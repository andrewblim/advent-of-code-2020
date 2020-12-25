from .context import advent_of_code_2020
from advent_of_code_2020.day25 import *


def test_transform():
    assert transform(subject=7, loop_size=8) == 5764801
    assert transform(subject=7, loop_size=11) == 17807724
    assert transform(subject=17807724, loop_size=8) == 14897079
    assert transform(subject=5764801, loop_size=11) == 14897079


def test_find_loop_size():
    assert find_loop_size(subject=7, key=5764801) == 8
    assert find_loop_size(subject=7, key=17807724) == 11


def test_find_encryption_key():
    assert find_encryption_key(5764801, 17807724, subject=7) == 14897079
