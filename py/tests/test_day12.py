from .context import advent_of_code_2020
from advent_of_code_2020.day12 import *
import pytest


test_moves = """
F10
N3
F7
R90
F11
""".strip()


def test_update_position():
    moves = [parse_move(x) for x in test_moves.splitlines()]
    assert update_position_after_moves((0, 0, 0), moves, update_position) == \
        pytest.approx((17, -8, 270))


def test_update_position2():
    moves = [parse_move(x) for x in test_moves.splitlines()]
    assert update_position_after_moves((0, 0, 10, 1), moves, update_position2) == \
        pytest.approx((214, -72, 4, -10))
