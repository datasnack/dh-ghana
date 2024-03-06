from datalayers.datasources.meteostat_layer import MeteostatLayer

class MeteoMaxt(MeteostatLayer):

    def __init__(self):
        super().__init__()
        self.col_of_interest = 'tmax'

        self.format_suffix = "°C"

