import pandas as pd

from shapes.models import Shape
from datalayers.datasources.base_layer import BaseLayer


class WhoHospbeddens(BaseLayer):
    def __init__(self) -> None:
        super().__init__()

    def download(self):
        pass

    def process(self, shapes=None):
        if shapes is None:
            shapes = Shape.objects.all()

        df = pd.read_csv(self.get_data_path() / "GHA_who_hospbeddens.csv")

        for shape in shapes:
            pcode = shape.get_property("pcode")
            dfx = df[df["ADMIN0"] == pcode]

            for _, row in dfx.iterrows():
                self.add_value(shape, row["year"], row[self.key])
