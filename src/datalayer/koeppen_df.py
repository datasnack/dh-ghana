from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenDf(KoeppenLayer):
    def __init__(self) -> None:
        super().__init__()

        self.climate_types = [
            self.ClimateTypes.Dfa,
            self.ClimateTypes.Dfb,
            self.ClimateTypes.Dfc,
            self.ClimateTypes.Dfd,
        ]
