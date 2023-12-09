from Modules.Tile import Tile
from Modules.Sprite import Sprite
from random import choice

class Matrix:

    def __init__(self, n: int = 10, m: int = 10, sprites: list = []) -> None:
        self.mesh = [[Tile(sprites) for j in range(m)] for i in range(n)]
        self.is_first_time = True

    def find_tiles_with_lowest_entropy(self) -> list:
        # Check if it's the first time collapsing the mesh
        if self.is_first_time:
            self.is_first_time = False
            return [choice(choice(self.mesh))]

        # Find the lowest entropy and the tiles with that entropy
        rows = []
        for i in self.mesh:
            row = [len(j.options) for j in i if not j.is_collapsed]
            if len(row) != 0:
                rows.append(min(row))
        lowest_entropy = min(rows)
        tiles_to_collapse = []
        for i in self.mesh:
            for j in i:
                if len(j.options) == lowest_entropy:
                    tiles_to_collapse.append(j)
        return tiles_to_collapse

    def collapse_tile(self, tiles: list) -> None:
        # Pick a random tile from the list of tiles and collapse it
        tile = choice(tiles)
        tile.collapse()

        # Change the entropy of the surrounding tiles
        self.change_entropy_surrounding_tiles(tile)

    def change_entropy_surrounding_tiles(self, tile: Tile) -> None:
        # Get the position of the tile
        x, y = self.get_tile_position(tile)
        # print(f"({x}, {y})") # Test for positions

        # Get the surrounding tiles
        surrounding_tiles = self.get_surrounding_tiles(x, y)

        # Change the entropy of the surrounding tiles
        for i in surrounding_tiles:
            if surrounding_tiles[i] != None:
                match i:
                    case "north":
                        surrounding_tiles[i].options = list(set(surrounding_tiles[i].options) & tile.content.pairs["north"])
                    case "east":
                        surrounding_tiles[i].options = list(set(surrounding_tiles[i].options) & tile.content.pairs["east"])
                    case "south":
                        surrounding_tiles[i].options = list(set(surrounding_tiles[i].options) & tile.content.pairs["south"])
                    case "west":
                        surrounding_tiles[i].options = list(set(surrounding_tiles[i].options) & tile.content.pairs["west"])

    def get_tile_position(self, tile: Tile) -> tuple:
        for i in range(len(self.mesh)):
            for j in range(len(self.mesh[i])):
                if self.mesh[i][j] == tile:
                    return j, i

    def get_surrounding_tiles(self, x: int, y: int) -> dict:
        surrounding_tiles = {"north": None, "east": None, "south": None, "west": None}

        # Get the north tile
        if y != 0:
            if not self.mesh[y - 1][x].is_collapsed:
                surrounding_tiles["north"] = self.mesh[y - 1][x]
        # Get the south tile
        if y != len(self.mesh) - 1:
            if not self.mesh[y + 1][x].is_collapsed:
                surrounding_tiles["south"] = self.mesh[y + 1][x]

        # Get the east tile
        if x != len(self.mesh[y]) - 1:
            if not self.mesh[y][x + 1].is_collapsed:
                surrounding_tiles["east"] = self.mesh[y][x + 1]
        # Get the west tile
        if x != 0:
            if not self.mesh[y][x - 1].is_collapsed:
                surrounding_tiles["west"] = self.mesh[y][x - 1]
        return surrounding_tiles

    # This function is not needed anymore
    # def everything_is_collapsed(self) -> bool:
    #     for i in self.mesh:
    #         for j in i:
    #             if not j.is_collapsed:
    #                 return False
    #     return True

    def print_map(self):
        for i in self.mesh:
            for j in i:
                # print(f"{j.content}:{len(j.options)}", end=" ") # Test for entropy
                # print(f"'{j.content}'", end="") # Test for sprites
                print(f"{j.content}", end="")
            print()