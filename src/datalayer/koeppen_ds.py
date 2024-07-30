from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenDs(KoeppenLayer):
    def __init__(self) -> None:
        super().__init__()

        self.climate_types = [
            self.ClimateTypes.Dsa,
            self.ClimateTypes.Dsb,
            self.ClimateTypes.Dsc,
            self.ClimateTypes.Dsd,
        ]
