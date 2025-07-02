import datetime as dt
import os
import re
import subprocess
from urllib.parse import urlparse

import numpy as np

from datalayers.datasources.base_layer import LayerTimeResolution, LayerValueType
from datalayers.datasources.tiff_layer import TiffLayer

RESOLUTION = "p05"  # p04 or p25 resolution in deg
BASE_URL = "https://data.chc.ucsb.edu/products/CHIRPS-2.0/africa_daily/tifs/{resolution}/{year}/chirps-v2.0.{year}.{month:02d}.{day:02d}.tif.gz"


class ChirpsPrcp(TiffLayer):
    def __init__(self) -> None:
        super().__init__()
        self.value_type = LayerValueType.FLOAT
        self.time_col = LayerTimeResolution.DAY
        self.manual_nodata = -9999

        self.chart_type = "bar"

        self.format_suffix = "mm"

    def download(self):
        start_date = dt.date(2015, 1, 1)
        end_date = dt.date(2024, 7, 1)

        # download all required files
        for date in self.date_range(start_date, end_date):
            url = BASE_URL.format(
                resolution=RESOLUTION, year=date.year, month=date.month, day=date.day
            )

            # does unzipped file already exists?
            # the gzip command for extracting deletes the .gz archive
            a = urlparse(url)
            file_name = os.path.basename(a.path)
            if os.path.isfile(
                self.get_data_path() / file_name.replace(".tif.gz", ".tif")
            ):
                continue

            # if file could not be downloaded, try to download without
            # .gz extension. For 2021-12-* all files are uncompressed
            if not self._save_url_to_file(url):
                self._save_url_to_file(url.replace("tif.gz", "tif"))

        # after, gzip all downloaded *.gz files
        # only keep extracted files
        # Raises a Warning/Exception when no *.gz files are found
        try:
            # the subprocess.check_output() syntax didn't work. why?
            # But subprocess.run did work.
            subprocess.run(
                f"gzip -d {self.get_data_path()}/*.gz",
                shell=True,
                encoding="UTF-8",
                capture_output=True,
                check=True,
            )
        except subprocess.CalledProcessError as error:
            self.layer.warning("Could not unzip files: %s", {"error_msg": error.output})

    def date_range(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + dt.timedelta(n)

    def consume(self, file, band, shape):
        x = re.search(
            r"([0-9]{4})\.([0-9]{2})\.([0-9]{2})\.tif", os.path.basename(file)
        )
        date = dt.date(int(x[1]), int(x[2]), int(x[3]))

        self.add_value(shape, date, np.nanmean(band))
