from datalayers.datasources.dhs_layer import DhsLayer
from datalayers.datasources.base_layer import LayerValueType


class DhsWaterimprov(DhsLayer):
    def __init__(self) -> None:
        super().__init__()
        self.value_type = LayerValueType.PERCENTAGE

    def get_indicators(self) -> list[str]:
        return ["WS_SRCE_P_IMP"]

    def get_countries(self) -> list[str]:
        return ["GH"]
