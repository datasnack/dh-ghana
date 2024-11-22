from .worldpop_age import WorldpopAge


class WorldpopAge65(WorldpopAge):
    def __init__(self) -> None:
        super().__init__()

    def get_ages(self) -> list[int]:
        return [65, 70, 75, 80]
