from .worldpop_age import WorldpopAge


class WorldpopAge1549(WorldpopAge):
    def __init__(self) -> None:
        super().__init__()

    def get_ages(self) -> list[int]:
        return [15, 20, 25, 30, 35]
