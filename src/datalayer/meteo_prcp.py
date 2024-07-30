from .meteo import Meteo


class MeteoPrcp(Meteo):
    def __init__(self) -> None:
        super().__init__()
        self.col_of_interest = "prcp"

        self.format_suffix = "mm"
