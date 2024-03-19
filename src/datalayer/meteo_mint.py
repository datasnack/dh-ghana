from datalayers.datasources.meteostat_layer import MeteostatLayer


class MeteoMint(MeteostatLayer):

    def __init__(self):
        super().__init__()
        self.col_of_interest = 'tmin'
        self.format_suffix = "°C"
