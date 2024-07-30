from datalayers.datasources.koeppen_layer import KoeppenLayer


class KoeppenBw(KoeppenLayer):
    def __init__(self) -> None:
        super().__init__()

        self.climate_types = [self.ClimateTypes.BWh, self.ClimateTypes.BWk]
