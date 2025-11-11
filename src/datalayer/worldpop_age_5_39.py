from .worldpop_age import WorldpopAge


class WorldpopAge539(WorldpopAge):
    def __init__(self) -> None:
        super().__init__()

    def get_ages(self) -> list[int]:
        return [5, 10, 15, 20, 25, 30, 35]
