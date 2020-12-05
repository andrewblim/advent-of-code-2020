from .context import advent_of_code_2020
from advent_of_code_2020.day05 import *


def test_seat():
    assert parse_seat("FBFBBFFRLR") == (44, 5)
    assert parse_seat("BFFFBBFRRR") == (70, 7)
    assert parse_seat("FFFBBBFRRR") == (14, 7)
    assert parse_seat("BBFFBBFRLL") == (102, 4)

    assert seat_id(parse_seat("FBFBBFFRLR")) == 357
    assert seat_id(parse_seat("BFFFBBFRRR")) == 567
    assert seat_id(parse_seat("FFFBBBFRRR")) == 119
    assert seat_id(parse_seat("BBFFBBFRLL")) == 820
