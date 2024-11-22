import geopandas
import pandas as pd

from datalayers.datasources.base_layer import BaseLayer
from datalayers.utils import get_engine
from shapes.models import Shape


class GhsReflab(BaseLayer):
    def __init__(self) -> None:
        super().__init__()
        self.raw_vector_data_table = "data_custom_covreflab"

    def download(self):
        df = pd.read_csv(
            self.get_data_path() / "GhanaHub_custom_covreflab_20240318.csv", sep=";"
        )

        df = df.dropna(subset=["lat", "long"])

        gdf = geopandas.GeoDataFrame(
            df, geometry=geopandas.points_from_xy(df.long, df.lat), crs=4326
        )

        gdf.to_postgis(
            self.raw_vector_data_table, con=get_engine(), if_exists="replace"
        )

    def process(self, shapes=None, save_output=False, param_dir=None):
        if shapes is None:
            shapes = Shape.objects.all()

        gdf = self.get_vector_data_df()

        for shape in shapes:
            gdfx = gdf[gdf["geometry"].within(shape.shapely_geometry())]
            self.rows.append({"year": 2024, "shape_id": shape.id, "value": len(gdfx)})

        self.save()
