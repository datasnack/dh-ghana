from datalayers.datasources.copernicus_layer import CopernicusLayer

class CopernicusBuilt(CopernicusLayer):

    def __init__(self):
        super().__init__()

        self.area_of_interest = [
            'built-up',
        ]
