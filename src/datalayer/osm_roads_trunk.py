import datetime as dt

import osmnx as ox

from datalayers.datasources.base_layer import BaseLayer, LayerValueType
from datalayers.utils import get_engine
from shapes.models import Shape


class OsmRoadsTrunk(BaseLayer):
    def __init__(self) -> None:
        super().__init__()

        self.value_type = LayerValueType.BINARY

        # table name for the cleaned records
        # can not be osm_airports. this name is used for the parameter!
        # but we want to store queried POIs as well
        self.raw_vector_data_table = "data_osm_roads_trunk"

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

        gdf.to_postgis(
            self.raw_vector_data_table, con=get_engine(), if_exists="replace"
        )

    def process(self, shapes=None):
        if shapes is None:
            shapes = Shape.objects.all()

        df = self.get_vector_data_df()

        for shape in shapes:
            dfx = df[df["geometry"].intersects(shape.shapely_geometry())]

            self.rows.append(
                {
                    "shape_id": shape.id,
                    "year": dt.datetime.now().year,
                    "value": len(dfx) > 0,
                }
            )

        self.save()
