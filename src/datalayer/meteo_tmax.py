from .meteo import Meteo


class MeteoTmax(Meteo):
    def __init__(self) -> None:
        super().__init__()
        self.col_of_interest = "tmax"
        self.format_suffix = "°C"
