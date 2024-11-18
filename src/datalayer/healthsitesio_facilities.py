import os
import subprocess

import geopandas
from shapely import wkt

from datalayers.datasources.base_layer import BaseLayer
from datalayers.utils import get_engine
from shapes.models import Shape


def make_unique(columns):
    seen = {}
    unique_cols = []
    for col in columns:
        if col not in seen:
            unique_cols.append(col)
            seen[col] = 1
        else:
            new_col = f"{col}_{seen[col]}"
            unique_cols.append(new_col)
            seen[col] += 1
    return unique_cols


class HealthsitesioFacilities(BaseLayer):
    def __init__(self) -> None:
        super().__init__()

        # table name for the cleaned records
        # can not be osm_airports. this name is used for the parameter!
        # but we want to store queried POIs as well
        self.raw_vector_data_table = "data_healthsitesio_facilities"

    def download(self):
        url = "https://healthsites.io/api/public/facilities/shapefile/Ghana/download"
        file_name = "Ghana.zip"

        if not os.path.isfile(self.get_data_path() / file_name):
            self._save_url_to_file(
                url, folder=self.get_data_path(), file_name=file_name
            )

        if not os.path.isfile(self.get_data_path() / "LICENSE.txt"):
            try:
                in_file = self.get_data_path() / file_name
                out_dir = self.get_data_path().as_posix()
                subprocess.run(
                    f"unzip {in_file} -d {out_dir}",
                    shell=True,
                    capture_output=True,
                    check=True,
                )
            except subprocess.CalledProcessError as error:
                self.layer.warning("Could not unzip files: %s", error.stderr)

        gdf = geopandas.read_file(self.get_data_path() / "Ghana-node.shp")
        gdf.columns = make_unique(gdf.columns)

        gdf.to_postgis(
            self.raw_vector_data_table,
            con=get_engine(),
            index=False,
            if_exists="replace",
        )

    def process(self, shapes=None, save_output=False, param_dir=None):
        if shapes is None:
            shapes = Shape.objects.all()

        gdf = geopandas.read_file(self.get_data_path() / "Ghana-node.shp")

        for shape in shapes:
            # get geometry of AoI
            mask = wkt.loads(shape.geometry.wkt)

            # clip to only facilities within AoI
            gdfx = gdf[gdf["geometry"].within(mask)]

            self.rows.append(
                {
                    "year": 2024,
                    "shape_id": shape.id,
                    "value": len(gdfx),  # <- count of facilities in AoI == len() of DF
                }
            )

        self.save()
