from datalayers.models import Datalayer
from datalayers.datasources.base_layer import (
    BaseLayer,
    LayerTimeResolution,
    LayerValueType,
)


class WorldpopPropAge65(BaseLayer):
    def __init__(self) -> None:
        super().__init__()
        self.value_type = LayerValueType.PERCENTAGE

    def download(self):
        pass

    def process(self, shapes):
        dl_worldpop_age = Datalayer.objects.get(key="worldpop_age_65")
        dl_worldpop_popc = Datalayer.objects.get(key="worldpop_popc")

        df_worldpop_age = dl_worldpop_age.data()
        df_worldpop_popc = dl_worldpop_popc.data()
        for shape in shapes:
            dfx_popc = df_worldpop_popc[df_worldpop_popc["shape_id"] == shape.id]

            for _, row in dfx_popc.iterrows():
                year = int(row["year"])

                dfx_worldpop_age = df_worldpop_age[
                    (df_worldpop_age["shape_id"] == shape.id)
                    & (df_worldpop_age["year"] == year)
                ].reset_index(drop=True)

                if len(dfx_worldpop_age) != 1:
                    continue

                self.add_value(
                    shape,
                    year,
                    dfx_worldpop_age.at[0, "value"] / row["value"],
                )
