from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)


class LitdataVectorcontrol(BaseLayer):
    def __init__(self) -> None:
        super().__init__()
        self.value_type = LayerValueType.BINARY

    def download(self):
        pass

    def process(self, shapes):
        for shape in shapes:
            if shape.type.key == "country":
                self.add_value(shape, 2024, True)
