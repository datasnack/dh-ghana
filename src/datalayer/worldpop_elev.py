import numpy as np

from datalayers.datasources.tiff_layer import TiffLayer


class WorldpopElev(TiffLayer):
    def __init__(self) -> None:
        super().__init__()
        self.format_suffix = "m"

    def download(self):
        self._save_url_to_file(
            "https://data.worldpop.org/GIS/Covariates/Global_2000_2020/GHA/Topo/gha_srtm_topo_100m.tif"
        )

    def consume(self, file, band, shape):
        year = 2000
        self.rows.append(
            {
                "year": year,
                "shape_id": shape.id,
                "value": np.nanmean(band),
                "value_min": np.nanmin(band),
                "value_max": np.nanmax(band),
                "value_std_dev": np.nanstd(band),
            }
        )
