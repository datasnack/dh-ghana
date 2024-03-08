from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenB(KoeppenLayer):

    def __init__(self):
        super().__init__()
        self.area_of_interest = [
            4,
            5,
            6,
            7
        ]
