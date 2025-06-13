import pandas as pd
import geopandas
from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)


class LitdataDenvLim2025(BaseLayer):
    def __init__(self) -> None:
        super().__init__()
        self.value_type: LayerValueType = LayerValueType.INTEGER
        self.raw_vector_data_table = True

    def download(self):
        url = "https://github.com/ahyoung-lim/Arbo_riskmaps_public/raw/refs/heads/main/data/raw_arbo_occ_data/den_occ.csv"
        self._save_url_to_file(url)

        df = pd.read_csv(self.get_data_path() / "den_occ.csv")
        df = df[df["disease"] == "dengue"]

        gdf = geopandas.GeoDataFrame(
            df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude), crs=4326
        )
        self.write_vector_data_to_db(gdf)

    def process(self, shapes):
        gdf = self.get_vector_data_df()

        for shape in shapes:
            mask = shape.shapely_geometry()
            gdfx = gdf[gdf["geometry"].within(mask)]

            year_counts = gdfx.groupby("Year").size()

            for year, count in year_counts.items():
                self.add_value(shape, year, count)
