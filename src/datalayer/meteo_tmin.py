from .meteo import Meteo


class MeteoTmin(Meteo):
    def __init__(self) -> None:
        super().__init__()
        self.col_of_interest = "tmin"
        self.format_suffix = "°C"
