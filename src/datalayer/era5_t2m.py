import geopandas
import pandas as pd
from shapely import wkt
import cdsapi
import xarray as xr

from shapes.models import Shape

from datalayers.datasources.base_layer import LayerValueType, LayerTimeResolution
from datalayers.datasources.base_layer import BaseLayer


class Era5T2m(BaseLayer):
    def __init__(self):
        super().__init__()

        self.time_col = LayerTimeResolution.DAY
        self.value_type = LayerValueType.VALUE

    def download(self):
        self._create_data_dir_if_not_exists()

        c = cdsapi.Client()

        c.retrieve(
            "reanalysis-era5-single-levels",
            {
                "product_type": "reanalysis",
                "format": "netcdf",
                "variable": "2m_temperature",
                "year": "2023",
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
                "time": [
                    "00:00",
                    "01:00",
                    "02:00",
                    "03:00",
                    "04:00",
                    "05:00",
                    "06:00",
                    "07:00",
                    "08:00",
                    "09:00",
                    "10:00",
                    "11:00",
                    "12:00",
                    "13:00",
                    "14:00",
                    "15:00",
                    "16:00",
                    "17:00",
                    "18:00",
                    "19:00",
                    "20:00",
                    "21:00",
                    "22:00",
                    "23:00",
                ],
                "area": [
                    11.17,
                    -3.26,
                    4.74,
                    1.2,
                ],
            },
            self.get_data_path() / "2023 2m_temperature.nz",
        )

    def process(self, shapes=None, save_output=False, param_dir=None):
        # get shapes
        if shapes is None:
            shapes = Shape.objects.all()

        # netCFD
        ds = xr.open_mfdataset(self.get_data_path() / "2023 2m_temperature.nz")

        # t2m is provided in Kelvin [K], transform to °C by subtracting 273.15
        # as specified in the Copernicus documentation
        ds["t2m"] -= 273.15
        ds["t2m"].attrs["units"] = "°C"

        # get points inside netCFD
        df = ds.isel(time=0).to_dataframe().reset_index()
        gdf_df_points = geopandas.GeoDataFrame(
            df,
            geometry=geopandas.points_from_xy(df.longitude, df.latitude),
            crs="EPSG:4326",
        )

        for shape in shapes:
            shape_geom = wkt.loads(shape.geometry.wkt)
            shape_points = gdf_df_points[gdf_df_points.within(shape_geom)]

            if len(shape_points) == 0:
                self.layer.warning("No points inside %s", {"shape_id": shape.id})
                continue

            # extract row for each point in the netCFD that is inside the
            # current shape
            datetime_index = ds.time.values
            point_series = []

            for i, row in shape_points.iterrows():
                lat = row["latitude"]
                lng = row["longitude"]

                point_series.append(ds.t2m.sel(longitude=lng, latitude=lat).values)

            # combine to data frame
            datetime_index = pd.to_datetime(datetime_index)
            df = pd.DataFrame(index=datetime_index)

            i = 1
            for s in point_series:
                df[f"p{i}"] = s
                i += 1

            # mean per time step
            df["mean"] = df.max(axis=1)

            # group to mean per day
            daily_df = df.groupby(pd.Grouper(freq="D")).max()

            for i, row in daily_df.iterrows():
                self.rows.append(
                    {
                        "date": i,
                        "value": row["mean"],
                        "shape_id": shape.id,
                    }
                )

        self.save()
