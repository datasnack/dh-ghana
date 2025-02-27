from datalayers.datasources.dhs_layer import DhsLayer
from datalayers.datasources.base_layer import LayerValueType


class DhsMediaMale(DhsLayer):
    def __init__(self) -> None:
        super().__init__()
        self.value_type = LayerValueType.PERCENTAGE

    def get_indicators(self) -> list[str]:
        return ["ED_MDIA_M_3MD"]

    def get_countries(self) -> list[str]:
        return ["GH"]

    def _mapping(self):
        """
        In 2018 Ghana created 6 new regions bei splitting up previous regions.

        Northern ->
            Northern
            North East
            Savannah

        Volta ->
            Volta
            Oti

        Western ->
            Western
            Western North

        Brong-Ahafo ->
            Bono
            Ahafo
            Bono East.


        """
        pass
