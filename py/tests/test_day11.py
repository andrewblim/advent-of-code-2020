from .context import advent_of_code_2020
from advent_of_code_2020.day11 import *


test_seats = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip().splitlines()

def test_updated_seats_and_changes():
    seats1, _ = updated_seats_and_changes(test_seats, updated_seat)
    assert seats1 == """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
    """.strip().splitlines()
    seats2, _ = updated_seats_and_changes(seats1, updated_seat)
    assert seats2 == """
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
    """.strip().splitlines()
    seats3, _ = updated_seats_and_changes(seats2, updated_seat)
    assert seats3 == """
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
    """.strip().splitlines()
    seats4, _ = updated_seats_and_changes(seats3, updated_seat)
    assert seats4 == """
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
    """.strip().splitlines()
    seats5, _ = updated_seats_and_changes(seats4, updated_seat)
    assert seats5 == """
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
    """.strip().splitlines()
    seats6, changes6 = updated_seats_and_changes(seats5, updated_seat)
    assert seats6 == seats5
    assert changes6 == 0
    assert count_occupied(seats6) == 37


def test_update_until_stable():
    seats, i = update_until_stable(test_seats, updated_seat)
    assert seats == """
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
    """.strip().splitlines()
    assert i == 5


def test_updated_seats_and_changes2():
    seats1, _ = updated_seats_and_changes(test_seats, updated_seat2)
    assert seats1 == """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
    """.strip().splitlines()
    seats2, _ = updated_seats_and_changes(seats1, updated_seat2)
    assert seats2 == """
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
    """.strip().splitlines()
    seats3, _ = updated_seats_and_changes(seats2, updated_seat2)
    assert seats3 == """
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
    """.strip().splitlines()
    seats4, _ = updated_seats_and_changes(seats3, updated_seat2)
    assert seats4 == """
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
    """.strip().splitlines()
    seats5, _ = updated_seats_and_changes(seats4, updated_seat2)
    assert seats5 == """
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
    """.strip().splitlines()
    seats6, _ = updated_seats_and_changes(seats5, updated_seat2)
    assert seats6 == """
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
    """.strip().splitlines()
    seats7, changes7 = updated_seats_and_changes(seats6, updated_seat2)
    assert seats7 == seats6
    assert changes7 == 0
    assert count_occupied(seats7) == 26
