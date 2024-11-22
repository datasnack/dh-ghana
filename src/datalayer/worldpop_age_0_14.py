from .worldpop_age import WorldpopAge


class WorldpopAge014(WorldpopAge):
    def __init__(self) -> None:
        super().__init__()

    def get_ages(self) -> list[int]:
        return [0, 1, 5, 10]
