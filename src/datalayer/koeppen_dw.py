from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenDw(KoeppenLayer):
    def __init__(self) -> None:
        super().__init__()

        self.climate_types = [
            self.ClimateTypes.Dwa,
            self.ClimateTypes.Dwb,
            self.ClimateTypes.Dwc,
            self.ClimateTypes.Dwd,
        ]
