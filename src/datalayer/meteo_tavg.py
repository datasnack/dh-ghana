from .meteo import Meteo


class MeteoTavg(Meteo):
    def __init__(self) -> None:
        super().__init__()
        self.col_of_interest = "tavg"
        self.format_suffix = "°C"
