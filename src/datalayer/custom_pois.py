import geopandas
import pandas as pd

from datalayers.utils import get_engine
from datalayers.datasources.base_layer import BaseLayer

class CustomPois(BaseLayer):

    def __init__(self):
        super().__init__()

        # table name for the cleaned records
        # can not be osm_airports. this name is used for the parameter!
        # but we want to store queried POIs as well
        self.raw_vector_data_table = 'data_custom_pois'

    def download(self):
        df = pd.read_csv(self.get_data_path() / 'data.csv')
        gdf = geopandas.GeoDataFrame(
            df, geometry=geopandas.points_from_xy(df.lng, df.lat))
        gdf = gdf.set_crs('epsg:4326')

        gdf.to_postgis(self.raw_vector_data_table, con=get_engine(), if_exists='replace')

