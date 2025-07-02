import datetime as dt

import osmnx as ox

from datalayers.datasources.base_layer import BaseLayer, LayerValueType


class OsmRoadsTrunk(BaseLayer):
    def __init__(self) -> None:
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

        G = ox.graph_from_polygon(
            shp, simplify=True, retain_all=True, custom_filter='["highway"~"trunk"]'
        )

        gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
        gdf_nodes = ox.io._stringify_nonnumeric_cols(gdf_nodes)
        gdf_edges = ox.io._stringify_nonnumeric_cols(gdf_edges)

        # flatten MultiIndex created by OSMnx
        gdf = gdf_edges.reset_index(drop=True)

        # drop all columns where each row is NULL
        gdf = gdf.dropna(axis=1, how="all")

        self.write_vector_data_to_db(gdf)

    def process(self, shapes=None):
        df = self.get_vector_data_df()

        for shape in shapes:
            dfx = df[df["geometry"].intersects(shape.shapely_geometry())]
            self.add_value(shape, dt.datetime.now().year, len(dfx) > 0)
