from datalayers.datasources.base_layer import BaseLayer, LayerTimeResolution

from shapes.models import Shape
from src.redcap.models import RedcapRecord


class RedcapTotal(BaseLayer):
    def __init__(self) -> None:
        super().__init__()
        self.time_col = LayerTimeResolution.DAY

    def download(self):
        pass

    def process(self):
        shapes = Shape.objects.all()
        records = RedcapRecord.objects.all()

        for shape in shapes:
            dates = {}

            for record in records:
                if shape.is_parent_of(record.shape):
                    if record.date not in dates:
                        dates[record.date] = 0

                    dates[record.date] += 1

            for date, count in dates.items():
                self.rows.append({"date": date, "shape_id": shape.id, "value": count})

        self.save()
