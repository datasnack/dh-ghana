import datetime as dt

from meteostat import Stations

from datalayers.datasources.meteostat_layer import MeteostatLayer


class Meteo(MeteostatLayer):
    def stations(self) -> Stations:
        stations = Stations()
        stations = stations.region("GH")
        return stations

    def start() -> dt.datetime:
        return dt.datetime(2010, 1, 1, tzinfo=dt.UTC)

    def end() -> dt.datetime:
        return dt.datetime.now(tz=dt.UTC)
