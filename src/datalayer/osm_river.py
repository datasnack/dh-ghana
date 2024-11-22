import datetime as dt

import fiona
import geopandas
import osmnx as ox
import pandas as pd
from shapely import wkt

from shapes.models import Shape
from datalayers.utils import get_engine
from datalayers.datasources.base_layer import BaseLayer


class OsmRiver(BaseLayer):
    def __init__(self):
        super().__init__()

        # table name for the cleaned records
        # can not be osm_airports. this name is used for the parameter!
        # but we want to store queried POIs as well
        self.raw_vector_data_table = "data_osm_river"

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

        gdf.to_postgis(
            self.raw_vector_data_table, con=get_engine(), if_exists="replace"
        )

    def process(self, shapes=None, save_output=False):
        if shapes is None:
            shapes = Shape.objects.all()

        # load imported data
        df = geopandas.read_postgis(
            f"SELECT * FROM {self.raw_vector_data_table}",
            geom_col="geometry",
            con=get_engine(),
        )

        dfs = []

        for shape in shapes:
            if isinstance(shape, Shape):
                # Shape uses the GeoDjango Model and so has not a shapely geometry
                # so convert it. amazing right?
                mask = [wkt.loads(shape.geometry.wkt)]
            elif "geometry" in shape:
                mask = [shape["geometry"]]
            elif "file" in shape:
                with fiona.open(shape["file"], "r") as shapefile:
                    mask = [feature["geometry"] for feature in shapefile]
            else:
                raise ValueError("No geometry found for given shape.")

            # clip to only POIs within area of interest
            dfx = df[df["geometry"].intersects(mask[0])]

            # group / count matching facilities per year
            has_rail = 0
            if len(dfx) > 0:
                has_rail = (
                    1.9  # https://www.theglobaleconomy.com/rankings/railroad_quality/
                )

            dfs.append(
                {
                    "shape_id": shape.id,
                    "year": dt.datetime.now().year,
                    "value": has_rail,
                }
            )

        dfsx = pd.DataFrame(dfs)
        dfsx.to_sql(self.layer.key, con=get_engine(), if_exists="replace")
