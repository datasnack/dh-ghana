import pandas as pd

from shapes.models import Shape
from datalayers.datasources.base_layer import BaseLayer


class WhoCommhealthwork(BaseLayer):
    def __init__(self) -> None:
        super().__init__()

    def download(self):
        pass

    def process(self, shapes=None):
        if shapes is None:
            shapes = Shape.objects.all()

        df = pd.read_csv(self.get_data_path() / "GHA_who_commhealthwork.csv")

        for shape in shapes:
            pcode = shape.get_property("pcode")
            dfx = df[df["ADMIN0"] == pcode]

            for i, row in dfx.iterrows():
                self.rows.append(
                    {"year": row["year"], "shape_id": shape.id, "value": row[self.key]}
                )

        self.save()
