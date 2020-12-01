from .context import advent_of_code_2020
from advent_of_code_2020.day01 import *


def test_find_sum():
    vals = [1721, 979, 366, 299, 675, 1456]
    assert find_sum_pair(vals, 2020) == (1721, 299)
    assert find_sum_triplet(vals, 2020) == (979, 366, 675)
