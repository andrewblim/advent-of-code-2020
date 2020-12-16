from .context import advent_of_code_2020
from advent_of_code_2020.day15 import *


def test_get_sequence():
    seq = [get_sequence([0,3,6], x) for x in range(1, 11)]
    assert seq == [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]
    assert get_sequence([0,3,6], 2020) == 436
    # these are slow, wish I had a better implementation
    assert get_sequence([0,3,6], 30000000) == 175594
    assert get_sequence([1,3,2], 30000000) == 2578
    assert get_sequence([2,1,3], 30000000) == 3544142
    assert get_sequence([1,2,3], 30000000) == 261214
    assert get_sequence([2,3,1], 30000000) == 6895259
    assert get_sequence([3,2,1], 30000000) == 18
    assert get_sequence([3,1,2], 30000000) == 362
