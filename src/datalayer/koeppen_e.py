from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenE(KoeppenLayer):

    def __init__(self):
        super().__init__()
        self.area_of_interest = [*range(29, 30+1)]
