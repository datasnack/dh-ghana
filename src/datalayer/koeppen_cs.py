from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenCs(KoeppenLayer):
    def __init__(self) -> None:
        super().__init__()

        self.climate_types = [
            self.ClimateTypes.Csa,
            self.ClimateTypes.Csb,
            self.ClimateTypes.Csc,
        ]
