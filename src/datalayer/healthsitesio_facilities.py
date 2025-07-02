import os
import subprocess

import geopandas

from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)


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
        self.value_type = LayerValueType.INTEGER
        self.time_col = LayerTimeResolution.YEAR
        self.raw_vector_data_table = True

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

        self.write_vector_data_to_db(gdf)

    def process(self, shapes):
        gdf = self.get_vector_data_df()

        for shape in shapes:
            # clip to only facilities within AoI
            gdfx = gdf[gdf["geometry"].within(shape.shapely_geometry())]

            self.add_value(shape, 2024, len(gdfx))
