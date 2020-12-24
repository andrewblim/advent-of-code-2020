from .context import advent_of_code_2020
from advent_of_code_2020.day23 import *


def test_play_cups():
    cups = DictCircularLL([3, 8, 9, 1, 2, 5, 4, 6, 7])
    make_move(cups)
    assert cups.to_list() == [2, 8, 9, 1, 5, 4, 6, 7, 3]
    make_move(cups)
    assert cups.to_list() == [5, 4, 6, 7, 8, 9, 1, 3, 2]
    make_move(cups)
    assert cups.to_list() == [8, 9, 1, 3, 4, 6, 7, 2, 5]
    make_move(cups)
    assert cups.to_list() == [4, 6, 7, 9, 1, 3, 2, 5, 8]
    make_move(cups)
    assert cups.to_list() == [1, 3, 6, 7, 9, 2, 5, 8, 4]
    make_move(cups)
    assert cups.to_list() == [9, 3, 6, 7, 2, 5, 8, 4, 1]


def test_play_cups2():
    cups = DictCircularLL([3, 8, 9, 1, 2, 5, 4, 6, 7] + list(range(10, 1_000_001)))
    for i in range(10_000_000):
        make_move(cups)
    assert cups.nodes[1][1] == 934001
    assert cups.nodes[934001][1] == 159792
