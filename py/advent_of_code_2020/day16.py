import sys
import re
from functools import reduce


def parse_ticket(ticket_text):
    return [int(x) for x in ticket_text.split(",")]


def parse_notes(notes):
    fields_text, your_ticket_text, nearby_tickets_text = notes.split("\n\n")
    fields = {}
    for line in fields_text.splitlines():
        name, range_text = line.split(": ")
        fields[name] = []
        for range in range_text.split(" or "):
            x, y = range.split("-")
            fields[name].append((int(x), int(y)))
    your_ticket = parse_ticket(your_ticket_text.splitlines()[1])
    nearby_tickets = [parse_ticket(x) for x in nearby_tickets_text.splitlines()[1:]]
    return (fields, your_ticket, nearby_tickets)


def invalid_entries(ticket, fields):
    all_ranges = [y for x in fields.values() for y in x]
    return [x for x in ticket
            if not any([lower <= x <= upper
                        for lower, upper in all_ranges])]


def valid_for(ticket, fields):
    entries = []
    for x in ticket:
        valids = set()
        for k, ranges in fields.items():
            if any([lower <= x <= upper for lower, upper in ranges]):
                valids.add(k)
        entries.append(valids)
    return entries


def identify_fields(tickets, fields):
    identified = [None] * len(fields)
    relevant_fields = dict(fields)
    while len(relevant_fields) > 0:
        validities = [valid_for(ticket, relevant_fields) for ticket in tickets]
        validities = [v for v in validities if all([len(x) > 0 for x in v])]
        possibs = [reduce(lambda x, y: x & y, v) for v in zip(*validities)]
        prev_n = len(relevant_fields)
        for i, x in enumerate(possibs):
            if identified[i] is not None:
                continue
            if len(x) == 0:
                raise RuntimeError("No possible values")
            elif len(x) == 1:
                identified[i] = x.pop()
                del relevant_fields[identified[i]]
        if len(relevant_fields) == prev_n:
            raise RuntimeError("No progress")
    return identified


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        notes = fp.read().strip()
    print("Part 1:")
    fields, your_ticket, nearby_tickets = parse_notes(notes)
    invalids = [invalid_entries(x, fields) for x in nearby_tickets]
    print(sum([y for x in invalids for y in x]))
    print("Part 2:")
    identified = identify_fields(nearby_tickets, fields)
    ided_ticket = {k: v for k, v in zip(identified, your_ticket)
                   if k.startswith("departure")}
    print(ided_ticket)
    print(reduce(lambda x, y: x * y, ided_ticket.values()))
