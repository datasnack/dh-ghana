import re
import os
import numpy as np

from datalayers.datasources.tiff_layer import TiffLayer
from datalayers.datasources.base_layer import BaseLayer, LayerValueType


class WorldpopPopd(TiffLayer):
    def __init__(self):
        super().__init__()
        self.value_type = LayerValueType.FLOAT
        self.format_suffix = "entities/km²"

    def download(self):
        for year in range(2010, 2020 + 1):
            url = f"https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/{year}/GHA/gha_pd_{year}_1km_UNadj.tif"
            self._save_url_to_file(url)

    def consume(self, file, band, shape):
        x = re.search(r"[0-9]+", os.path.basename(file))
        year = int(x[0])

        self.add_value(shape, year, np.nanmean(band))
