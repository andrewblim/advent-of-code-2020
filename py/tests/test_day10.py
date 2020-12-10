from .context import advent_of_code_2020
from advent_of_code_2020.day10 import *


test_adapters1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
test_adapters2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                  38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
test_adapters1.sort()
test_adapters2.sort()

def test_jolt_diffs_on_full_chain():
    assert jolt_diffs_on_full_chain(test_adapters1) == [7, 0, 5]
    assert jolt_diffs_on_full_chain(test_adapters2) == [22, 0, 10]


def test_legal_chains():
    assert legal_chains(test_adapters1) == 8
    assert legal_chains(test_adapters2) == 19208
