from .context import advent_of_code_2020
from advent_of_code_2020.day09 import *


test_code = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_check_xmas_code():
    assert check_xmas_code(test_code, 5) == 127


def test_find_contiguous_sum():
    start, end = find_contiguous_sum(test_code, 127)
    assert test_code[start:(end+1)] == [15, 25, 47, 40]
