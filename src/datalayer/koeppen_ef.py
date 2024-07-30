from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenEf(KoeppenLayer):
    def __init__(self) -> None:
        super().__init__()

        self.climate_types = [
            self.ClimateTypes.EF,
        ]
