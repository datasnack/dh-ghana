from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenC(KoeppenLayer):

    def __init__(self):
        super().__init__()
        self.area_of_interest = [*range(8, 16+1)]
