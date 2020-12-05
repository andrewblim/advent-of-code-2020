import sys


def parse_seat(input):
    return (parse_row(input[0:7]), parse_aisle(input[7:10]))


def parse_row(input):
    return sum([2**i if x == "B" else 0 for i, x in enumerate(reversed(input))])


def parse_aisle(input):
    return sum([2**i if x == "R" else 0 for i, x in enumerate(reversed(input))])


def seat_id(seat):
    return seat[0]*8 + seat[1]


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        ids = [seat_id(parse_seat(x.strip())) for x in fp.readlines()]
    print("Part 1:")
    print(max(ids))
    print("Part 2:")
    ids.sort()
    for id1, id2 in zip(ids, ids[1:]):
        if id2 != id1 + 1:
            print(id2-1)
            break
