from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenD(KoeppenLayer):

    def __init__(self):
        super().__init__()
        self.area_of_interest = [*range(17, 28+1)]
