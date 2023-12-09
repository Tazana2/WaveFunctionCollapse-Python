from Modules.Matrix import Matrix
from Modules.Sprite import Sprite
import os, time

if __name__ == "__main__":
    # Create the sprites
    a = Sprite(" ")
    b = Sprite("┴")
    c = Sprite("├")
    d = Sprite("┬")
    e = Sprite("┤")
    # blue = Sprite("🟦")
    # green = Sprite("🟩")

    # Add the sprites that can be with others in this order: Noth - East - South - West
    a.add_pairs({a, b}, {a, c}, {a, d}, {a, e})
    b.add_pairs({c, d, e}, {b, d, e}, {a, d}, {b, c, d, e})
    c.add_pairs({c, d, e}, {b, d, e}, {b, c, e}, {a, e})
    d.add_pairs({a, b}, {b, d, e}, {b, c, e}, {b, c, d, e})
    e.add_pairs({c, d, e}, {a, c}, {b, c, e}, {b, c, d})
    # blue.add_pairs({a}, {a}, {a, b}, {a, b}) 
    # green.add_pairs({a, b}, {a, b}, {b}, {b})

    # Create a map with NxM tiles with the sprites
    n, m = 30, 30
    my_map = Matrix(n, m, [a, b, c, d, e])
    # my_map = Matrix(m, n, [blue, green])

    start = time.time()

    # Collapse the map
    for _ in range(m*n):
        os.system("cls")
        # Find the tiles with the lowest entropy
        tiles_to_collapse = my_map.find_tiles_with_lowest_entropy()

        # Collapse the tiles
        my_map.collapse_tile(tiles_to_collapse)

        # Print the map while it's collapsing
        my_map.print_map()

    end = time.time()
    print(end - start)