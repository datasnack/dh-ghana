import datetime as dt

import osmnx as ox

from datalayers.datasources.base_layer import BaseLayer, LayerValueType
from datalayers.utils import get_engine
from shapes.models import Shape


class OsmPorts(BaseLayer):
    def __init__(self) -> None:
        super().__init__()

        self.value_type = LayerValueType.VALUE

        # table name for the cleaned records
        # can not be osm_airports. this name is used for the parameter!
        # but we want to store queried POIs as well
        self.raw_vector_data_table = "data_osm_ports"

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

        gdf.to_postgis(
            self.raw_vector_data_table, con=get_engine(), if_exists="replace"
        )

    def process(self, shapes=None):
        if shapes is None:
            shapes = Shape.objects.all()

        # load imported data
        df = self.get_vector_data_df()

        for shape in shapes:
            # clip to only POIs within area of interest
            dfx = df[df["geometry"].within(shape.shapely_geometry())]

            self.rows.append(
                {
                    "shape_id": shape.id,
                    "year": dt.datetime.now().year,
                    "value": len(dfx),
                }
            )

        self.save()
