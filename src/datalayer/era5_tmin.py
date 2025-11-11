import datetime as dt

import cdsapi
import geopandas
import pandas as pd
import rioxarray
import xarray as xr
from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)
from shapely import wkt


class Era5Tmin(BaseLayer):
    def __init__(self):
        super().__init__()

        self.time_col = LayerTimeResolution.DAY
        self.value_type = LayerValueType.VALUE

    def download(self):
        self._create_data_dir_if_not_exists()

        geom = self._get_convex_hull_from_db()
        # apply 0.25deg buffer around convex hull. 0.25 is the grid size of ERA5.
        # by doing so we make sure the complete area is covered and nothing is cut off
        # due do the nearest cell being deeper inside the area.
        geom = geom.buffer(0.25)
        west, south, east, north = geom.bounds
        era5_area = [north, west, south, east]

        dataset = "derived-era5-single-levels-daily-statistics"
        request = {
            "product_type": "reanalysis",
            "variable": ["2m_temperature"],
            "year": "2024",
            "month": [
                "01",
                "02",
                "03",
                "04",
                "05",
                "06",
                "07",
                "08",
                "09",
                "10",
                "11",
                "12",
            ],
            "day": [
                "01",
                "02",
                "03",
                "04",
                "05",
                "06",
                "07",
                "08",
                "09",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
                "31",
            ],
            "daily_statistic": "daily_minimum",
            "time_zone": "utc+00:00",
            "frequency": "1_hourly",
            "area": era5_area,
        }

        client = cdsapi.Client()
        for year in range(2020, 2025 + 1):
            request["year"] = year
            client.retrieve(
                dataset, request, self.get_data_path() / f"{year}_2m_temperature_min.nc"
            )

    def process(self, shapes):
        nc_files = self.get_data_path().glob("*.nc")

        for nc in nc_files:
            ds = xr.open_dataset(nc)
            era5_var = ds["t2m"]

            # ERA5 is WGS84/EPSG:4326
            era5_var.rio.write_crs("EPSG:4326", inplace=True)

            for t in era5_var.valid_time:
                dt_day = dt.date(int(t.dt.year), int(t.dt.month), int(t.dt.day))
                time_data = era5_var.sel(valid_time=t)

                for shape in shapes:
                    try:
                        clipped_data = time_data.rio.clip(
                            [shape.shapely_geometry()], "EPSG:4326"
                        )
                    except rioxarray.exceptions.NoDataInBounds:
                        # in case no raster cell centers are inside the geometry of the
                        # shape, select the nearest value to the centroid of the shape
                        centroid = shape.shapely_geometry().centroid
                        clipped_data = time_data.sel(
                            latitude=centroid.y, longitude=centroid.x, method="nearest"
                        )
                        self.layer.warning(
                            "No cells inside geometry, fallback to nearest cell center",
                            {"shape_id": shape.id},
                        )

                    mean_kelvin = clipped_data.mean(skipna=True).to_numpy().item()

                    self.add_value(
                        shape,
                        dt_day,
                        # data are in K, convert to C
                        mean_kelvin - 273.15,
                    )

        # print(f"No data for {shape} at {dt_day}")
