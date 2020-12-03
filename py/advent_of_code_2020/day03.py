import sys
from functools import reduce


def parse_map_line(line):
    return [1 if c == "#" else 0 for c in line]


def count_trees(map, dir_change, start=(0, 0)):
    trees = 0
    pos = start
    for i, row in enumerate(map):
        if i == pos[1]:
            trees += row[pos[0] % len(row)]
            pos = (pos[0] + dir_change[0], pos[1] + dir_change[1])
    return trees


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        map = [parse_map_line(line.rstrip()) for line in fp.readlines()]
    print("Part 1:")
    print(count_trees(map, (3, 1)))
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [count_trees(map, x) for x in slopes]
    print(trees)
    print(reduce(lambda x, y: x*y, trees))
