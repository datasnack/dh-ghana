from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenCf(KoeppenLayer):
    def __init__(self) -> None:
        super().__init__()

        self.climate_types = [
            self.ClimateTypes.Cfa,
            self.ClimateTypes.Cfb,
            self.ClimateTypes.Cfc,
        ]
