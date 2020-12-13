from .context import advent_of_code_2020
from advent_of_code_2020.day13 import *


test_info = """
939
7,13,x,x,59,x,31,19
""".strip()


def test_update_position():
    ready, buses = parse_input(test_info)
    bus, depart = earliest_bus_possible_info(ready, buses)
    assert bus == 59
    assert depart == 944


def test_find_earliest_timestamp():
    _, buses = parse_input("0\n17,x,13,19")
    assert(find_earliest_timestamp(buses)) == 3417
    _, buses = parse_input("0\n67,7,59,61")
    assert(find_earliest_timestamp(buses)) == 754018
    _, buses = parse_input("0\n67,x,7,59,61")
    assert(find_earliest_timestamp(buses)) == 779210
    _, buses = parse_input("0\n67,7,x,59,61")
    assert(find_earliest_timestamp(buses)) == 1261476
    _, buses = parse_input("0\n1789,37,47,1889")
    assert(find_earliest_timestamp(buses)) == 1202161486
