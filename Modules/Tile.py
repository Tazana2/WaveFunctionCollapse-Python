import random

class Tile:
    def __init__(self, options: list) -> None:
        # self.content = "⬛"
        self.content = " "
        self.is_collapsed = False
        self.options = options

    def collapse(self) -> None:
        # Change the status of the tile to collapsed
        self.is_collapsed = True

        # Pick a random Sprite from the list of options
        if self.options:
            self.content = random.choice(self.options)
            self.options = []

    def __str__(self) -> str:
        return self.content