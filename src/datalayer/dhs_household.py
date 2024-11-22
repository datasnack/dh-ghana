from datalayers.datasources.dhs_layer import DhsLayer
from datalayers.datasources.base_layer import LayerValueType


class DhsHousehold(DhsLayer):
    def __init__(self) -> None:
        super().__init__()

    def get_indicators(self) -> list[str]:
        return ["HC_MEMB_H_MNM"]

    def get_countries(self) -> list[str]:
        return ["GH"]
