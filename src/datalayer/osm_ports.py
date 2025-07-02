import datetime as dt

import osmnx as ox

from datalayers.datasources.base_layer import BaseLayer, LayerValueType


class OsmPorts(BaseLayer):
    def __init__(self) -> None:
        super().__init__()
        self.value_type = LayerValueType.INTEGER
        self.raw_vector_data_table = True

    def download(self):
        ox.settings.log_console = True
        ox.settings.use_cache = True
        ox.settings.cache_folder = self.get_data_path()
        ox.settings.timeout = 1800

        # get convex hull for all loaded shapes
        shp = self._get_convex_hull_from_db()

        # OSM ferry terminals
        gdf = ox.features_from_polygon(
            shp,
            {"amenity": "ferry_terminal"},
        )

        # flatten MultiIndex created by OSMnx
        gdf = gdf.reset_index(drop=True)

        # Some airports are stored as OSM ways/paths. But wie only want a POINT.
        # Centroid might be outside the polygon (runways), but still in the
        # airport vicinity, so this is Okay.
        # polygon -> centroid
        #
        # Use a projected CRS for the centroid, this maps the coordinate on a
        # flat map, instead of a geographic CRS which has earths curves in it.
        # -> projected CRS is will yield more accurate results.
        gdf["geometry"] = gdf["geometry"].to_crs("+proj=cea").centroid.to_crs(gdf.crs)

        # drop all columns where each row is NULL
        gdf = gdf.dropna(axis=1, how="all")

        self.write_vector_data_to_db(gdf)

    def process(self, shapes):
        df = self.get_vector_data_df()

        for shape in shapes:
            dfx = df[df["geometry"].within(shape.shapely_geometry())]
            self.add_value(shape, dt.datetime.now().year, len(dfx))
