class Sprite:
    def __init__(self, image) -> None:
        self.image = image
        self.pairs = {}

    def add_pairs(self, norht: set, east: set, south: set, west: set) -> None:
        self.pairs["north"] = norht
        self.pairs["east"] = east
        self.pairs["south"] = south
        self.pairs["west"] = west

    def __str__(self) -> str:
        return self.image