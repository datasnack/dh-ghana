from datalayers.datasources.copernicus_layer import CopernicusLayer

class CopernicusSparse(CopernicusLayer):

    def __init__(self):
        super().__init__()

        self.area_of_interest = [
            'bare_sparse_vegetation',
        ]
