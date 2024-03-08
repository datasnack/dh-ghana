from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenA(KoeppenLayer):

    def __init__(self):
        super().__init__()

        # tropical
        self.area_of_interest = [
            1,
            2,
            3
        ]
