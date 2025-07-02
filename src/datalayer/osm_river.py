import datetime as dt

import osmnx as ox

from datalayers.datasources.base_layer import BaseLayer, LayerValueType


class OsmRiver(BaseLayer):
    def __init__(self):
        super().__init__()
        self.value_type = LayerValueType.BINARY
        self.raw_vector_data_table = True

    def download(self):
        ox.settings.log_console = True
        ox.settings.use_cache = True
        ox.settings.cache_folder = self.get_data_path()
        ox.settings.timeout = 1800

        # get convex hull for all loaded shapes
        shp = self._get_convex_hull_from_db()

        # OSM rivers: https://wiki.openstreetmap.org/wiki/Rivers
        #
        gdf = ox.geometries_from_polygon(
            shp, {"waterway": "river", "natural": "water", "water": "river"}
        )

        # flatten MultiIndex created by OSMnx
        gdf = gdf.reset_index(drop=True)

        # drop all columns where each row is NULL
        gdf = gdf.dropna(axis=1, how="all")

        self.write_vector_data_to_db(gdf)

    def process(self, shapes):
        df = self.get_vector_data_df()

        for shape in shapes:
            dfx = df[df["geometry"].intersects(shape.shapely_geometry())]
            self.add_value(shape, dt.datetime.now().year, len(dfx) > 0)
