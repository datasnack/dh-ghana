from datalayers.datasources.meteostat_layer import MeteostatLayer

class MeteoTprecit(MeteostatLayer):

    def __init__(self):
        super().__init__()
        self.col_of_interest = 'prcp'

        self.format_suffix = "mm"
