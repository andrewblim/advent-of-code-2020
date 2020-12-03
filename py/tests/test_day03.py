from .context import advent_of_code_2020
from advent_of_code_2020.day03 import *


def test_count_trees():
    map_data = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
    """.strip()
    map = [parse_map_line(line) for line in map_data.split("\n")]
    assert count_trees(map, (1, 1)) == 2
    assert count_trees(map, (3, 1)) == 7
    assert count_trees(map, (5, 1)) == 3
    assert count_trees(map, (7, 1)) == 4
    assert count_trees(map, (1, 2)) == 2
