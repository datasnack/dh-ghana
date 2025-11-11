import re
from pathlib import Path


import pandas as pd
import numpy as np

from datalayers.datasources.tiff_layer import TiffLayer


class WorldpopAge(TiffLayer):
    def __init__(self):
        super().__init__()
        self._tmp = {}

    def get_data_path(self) -> Path:
        return Path("./data/datalayers/worldpop_age/")

    def download(self):
        base_url = "https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020_Constrained_UNadj/{year}/GHA//gha_{sex}_{age}_{year}_constrained_UNadj.tif"

        # Constrained_UNadj is only available for 2020
        for year in range(2020, 2020 + 1):
            for sex in ["f", "m"]:
                for age in [
                    0,
                    1,
                    5,
                    10,
                    15,
                    20,
                    25,
                    30,
                    35,
                    40,
                    45,
                    50,
                    55,
                    60,
                    65,
                    70,
                    75,
                    80,
                ]:
                    url = base_url.format(year=year, age=age, sex=sex)
                    self._save_url_to_file(url)

    def consume(self, file, band, shape):
        x = re.search(r"([fm]{1})_([0-9]{1,2})_([0-9]{4})", file)

        sex = x[1]
        age = int(x[2])
        year = int(x[3])

        if age not in self.get_ages():
            return

        # we need to aggregate values provided by multiple consume() runs,
        # so we create a tmp data structure to aggregate them
        key = f"{year}_{shape.id}"
        if key in self._tmp:
            self._tmp[key]["value"] += np.nansum(band)
        else:
            self._tmp[key] = {
                "year": year,
                "shape_id": shape.id,
                "value": np.nansum(band),
            }

    def save(self):
        self.df = pd.DataFrame(self._tmp.values())
        super().save()

    def get_ages(self) -> list[int]:
        raise NotImplementedError
