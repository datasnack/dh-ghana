import numpy as np

from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)

from datalayers.datasources.tiff_layer import TiffLayer


class WorldpopElevation(TiffLayer):
    def __init__(self) -> None:
        super().__init__()

    def download(self):
        url = "https://data.worldpop.org/GIS/Covariates/Global_2015_2030/GHA/Elevation/MERIT_DEM/v1/gha_elevation_merit103_100m_v1.tif"
        self._save_url_to_file(url)

    def consume(self, file, band, shape):
        self.add_value(shape, 2007, np.nanmean(band))
