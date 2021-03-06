import sys
import re
from collections import namedtuple

PlacedTile = namedtuple("PlacedTile", ["id", "north", "south", "east", "west", "image"])


# edges are interpreted as 0/1, most significant digit first
def edge_to_int(edge):
    return sum([(1 << i) for i, x in enumerate(reversed(edge)) if x == "#"])


def flip_edge(x, n):
    y = 0
    for i in range(n):
        y <<= 1
        y += x % 2
        x >>= 1
    return y


def flip_image_horiz(image):
    return "\n".join([y[::-1] for y in image.split("\n")])


def flip_tile_horiz(x, n):
    return PlacedTile(
        id=x.id,
        north=flip_edge(x.north, n),
        south=flip_edge(x.south, n),
        east=x.west,
        west=x.east,
        image=flip_image_horiz(x.image),
    )


def rotate_image_cw(image):
    image = image.split("\n")
    x_max = len(image[0])
    y_max = len(image)
    return "\n".join(["".join([image[y_max-1-i][j]
                               for i in range(y_max)])
                      for j in range(x_max)])


def rotate_tile_cw(x, n):
    return PlacedTile(
        id=x.id,
        north=flip_edge(x.west, n),
        east=x.north,
        south=flip_edge(x.east, n),
        west=x.south,
        image=rotate_image_cw(x.image),
    )


def parse_tiles(input):
    tiles = []
    tile_texts = input.split("\n\n")
    for tile_text in tile_texts:
        tile_data = tile_text.split("\n")
        n = len(tile_data) - 1
        tile_id = int(re.match(r"^Tile (\d+):", tile_data[0])[1])
        edge_n = edge_to_int(tile_data[1])
        edge_s = edge_to_int(tile_data[n])
        edge_e = edge_to_int([x[n-1] for x in tile_data[1:]])
        edge_w = edge_to_int([x[0] for x in tile_data[1:]])
        tile = PlacedTile(
            id=tile_id,
            north=edge_n,
            east=edge_e,
            south=edge_s,
            west=edge_w,
            image="\n".join([x[1:(n-1)] for x in tile_data[2:n]]),
        )
        tiles.extend([tile, flip_tile_horiz(tile, n)])
        tile = rotate_tile_cw(tile, n)
        tiles.extend([tile, flip_tile_horiz(tile, n)])
        tile = rotate_tile_cw(tile, n)
        tiles.extend([tile, flip_tile_horiz(tile, n)])
        tile = rotate_tile_cw(tile, n)
        tiles.extend([tile, flip_tile_horiz(tile, n)])
    return tiles


# Store a zigzag array for conversion between n and (x,y)
def zigzag(n):
    result = []
    for i in range(n):
        for j in range(i+1):
            result.append((i-j, j))
    for i in range(n-2, -1, -1):
        for j in range(i, -1, -1):
            result.append((j+n-i-1, n-j-1))
    return result


def find_tiling(tiles, progress, n_to_xy, xy_to_n):
    if len(tiles) == 0:
        return progress
    x, y = n_to_xy[len(progress)]
    for tile in tiles:
        if (x == 0 or tile.west == progress[xy_to_n[(x-1, y)]].east) and \
           (y == 0 or tile.north == progress[xy_to_n[(x, y-1)]].south):
            result = find_tiling(
                [t for t in tiles if t.id != tile.id],
                progress + [tile],
                n_to_xy,
                xy_to_n,
            )
            if result is not None:
                return result


def combine_image(images, xy_to_n):
    combined = []
    n = int(len(images)**0.5)
    for y in range(n):
        row = []
        for x in range(n):
            row.append(images[xy_to_n[(x,y)]].split("\n"))
        combined.append(["".join(z) for z in zip(*row)])
    return "\n".join([y for x in combined for y in x])


def find_dragons(image):
    image_arr = image.split("\n")
    n = image.index("\n")  # assume square
    dragon_text = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   "
    locations = []
    for r in range(4):
        dragon = dragon_text.split("\n")
        coords = [(x, y) for y, row in enumerate(dragon) for x, c in enumerate(row)
                  if c == "#"]
        for y in range(n - len(dragon)):
            for x in range(n - len(dragon[0])):
                hits = [image_arr[p[1]+y][p[0]+x] == "#" for p in coords]
                if all(hits):
                    locations.extend([(p[0]+x, p[1]+y) for p in coords])
        dragon_text = rotate_image_cw(dragon_text)
    dragon_text = flip_image_horiz(dragon_text)
    for r in range(4):
        dragon = dragon_text.split("\n")
        coords = [(x, y) for y, row in enumerate(dragon) for x, c in enumerate(row)
                  if c == "#"]
        for y in range(n - len(dragon)):
            for x in range(n - len(dragon[0])):
                hits = [image_arr[p[1]+y][p[0]+x] == "#" for p in coords]
                if all(hits):
                    locations.extend([(p[0]+x, p[1]+y) for p in coords])
        dragon_text = rotate_image_cw(dragon_text)
    return set(locations)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = fp.read().strip()
    print("Part 1:")
    tiles = parse_tiles(input)
    n = int((len(tiles) // 8)**0.5)
    zz = zigzag(n)
    izz = {p: i for i, p in enumerate(zz)}
    tiling = find_tiling(tiles, [], zz, izz)
    corners = [
        tiling[izz[(0,0)]],
        tiling[izz[(n-1,0)]],
        tiling[izz[(0,n-1)]],
        tiling[izz[(n-1,n-1)]],
    ]
    print([x.id for x in corners])
    print(corners[0].id * corners[1].id * corners[2].id * corners[3].id)
    print("Part 2:")
    combined = combine_image([x.image for x in tiling], izz)
    dragon_points = find_dragons(combined)
    n_hash = len([x for x in combined if x == "#"])
    print(n_hash - len(dragon_points))
