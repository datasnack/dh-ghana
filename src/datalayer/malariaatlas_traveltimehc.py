import re
import os
import subprocess
from urllib.parse import urlparse

import numpy as np

from datalayers.datasources.tiff_layer import TiffLayer


class MalariaatlasTraveltimehc(TiffLayer):
    def __init__(self):
        super().__init__()
        self.precision = 3  # to small value for rounding
        self.format_suffix = "minutes"

    def download(self):
        urls = [
            "https://data.malariaatlas.org/geoserver/Accessibility/ows?service=CSW&version=2.0.1&request=DirectDownload&ResourceId=Accessibility:202001_Global_Motorized_Travel_Time_to_Healthcare"
        ]

        for url in urls:
            self._save_url_to_file(url)

            # Check if file is already unzipped
            a = urlparse(url)
            file_name = os.path.basename(a.path)

            if os.path.isfile(
                self.get_data_path()
                / "202001_Global_Motorized_Travel_Time_to_Healthcare_2019.tif"
            ):
                self.layer.debug("File already unzipped.")
                return
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

    def consume(self, file, band, shape):
        x = re.search(r"_([0-9]+)\.tif$", os.path.basename(file))
        year = int(x[1])

        self.add_value(shape, year, np.nanmean(band))
