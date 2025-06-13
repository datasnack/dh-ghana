import numpy as np

from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)
from datalayers.datasources.tiff_layer import TiffLayer


class LitmodDengueLim2025(TiffLayer):
    def __init__(self) -> None:
        super().__init__()

    def download(self):
        url = "https://github.com/ahyoung-lim/Arbo_riskmaps_public/raw/refs/heads/main/outputs/Rasters/DEN_riskmap_wmean_masked.tif"
        self._save_url_to_file(url)

    def consume(self, file, band, shape):
        mean = np.nanmean(band)

        # the value is derived from multiple historical records, most of them came
        # from 2015/2016 so we apply the calculated from that time until publication (2024).
        for year in range(2015, 2024 + 1):
            self.add_value(shape, year, mean)
