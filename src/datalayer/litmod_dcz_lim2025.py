import numpy as np
from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)
from datalayers.datasources.tiff_layer import TiffLayer


class LitmodDczLim2025(TiffLayer):
    def __init__(self) -> None:
        super().__init__()

    def download(self):
        url = "https://github.com/ahyoung-lim/Arbo_riskmaps_public/raw/refs/heads/main/outputs/Rasters/DCZ_binmap_mean.tif"
        self._save_url_to_file(url)

    def consume(self, file, band, shape):
        total_cells = np.count_nonzero(~np.isnan(band))
        values, count = np.unique(band, return_counts=True)
        stats = dict(zip(values, count, strict=True))

        aoi_cells = 0
        ones = np.float64(1.0)
        if ones in stats:
            aoi_cells = stats[ones]

        proportion = aoi_cells / total_cells

        # the value is derived from multiple historical records, most of them came
        # from 2015/2016 so we apply the calculated from that time until publication (2024).
        for year in range(2015, 2024 + 1):
            self.add_value(shape, year, proportion)
