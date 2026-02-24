import os
import re

import numpy as np
from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)
from datalayers.datasources.tiff_layer import TiffLayer


class FaoLivestockSheep(TiffLayer):
    def __init__(self) -> None:
        super().__init__()
        self.value_type: LayerValueType = LayerValueType.FLOAT

    def download(self):
        urls = [
            "https://storage.googleapis.com/fao-gismgr-glw4-2020-data/DATA/GLW4-2020/MAPSET/D-DA/GLW4-2020.D-DA.SHP.tif"
        ]

        for url in urls:
            self._save_url_to_file(url)

    def consume(self, file, band, shape):
        x = re.search(r"[0-9]{4}", os.path.basename(file))
        year = int(x[0])

        self.add_value(shape, year, np.nanmean(band))
