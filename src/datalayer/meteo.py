import datetime as dt

from meteostat import Stations

from datalayers.datasources.meteostat_layer import MeteostatLayer


class Meteo(MeteostatLayer):
    def stations(self) -> Stations:
        stations = Stations()
        stations = stations.region("GH")
        return stations

    def start(self) -> dt.datetime:
        return dt.datetime(2010, 1, 1)

    def end(self) -> dt.datetime:
        return dt.datetime.now()

    def get_vector_data_table(self):
        return "meteostat_stations"
