from .context import advent_of_code_2020
from advent_of_code_2020.day16 import *


test_notes = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip()

def test_parse_notes():
    fields, your_ticket, nearby_tickets = parse_notes(test_notes)
    assert fields == {
        "class": [(1,3), (5,7)],
        "row": [(6,11), (33,44)],
        "seat": [(13,40), (45,50)],
    }
    assert your_ticket == [7,1,14]
    assert nearby_tickets == [
        [7,3,47],
        [40,4,50],
        [55,2,20],
        [38,6,12],
    ]


def test_parse_tickets():
    fields, _, nearby_tickets = parse_notes(test_notes)
    invalids = [invalid_entries(x, fields) for x in nearby_tickets]
    assert invalids == [[], [4], [55], [12]]


test_notes2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
""".strip()

def test_valid_for():
    fields, _, nearby_tickets = parse_notes(test_notes2)
    validities = [valid_for(ticket, fields) for ticket in nearby_tickets]
    assert validities[0] == [
        {"row", "seat"},
        {"class", "row", "seat"},
        {"class", "row", "seat"},
    ]
    assert validities[1] == [
        {"class", "row"},
        {"class", "row", "seat"},
        {"class", "row", "seat"},
    ]
    assert validities[2] == [
        {"class", "row", "seat"},
        {"class", "row"},
        {"class", "row", "seat"},
    ]


def test_identify_fields():
    fields, your_ticket, nearby_tickets = parse_notes(test_notes2)
    identified = identify_fields(nearby_tickets, fields)
    ided_ticket = dict(zip(identified, your_ticket))
    assert ided_ticket == {"row": 11, "class": 12, "seat": 13}
