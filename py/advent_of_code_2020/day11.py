import sys


def updated_seat(seats, i, j):
    if seats[i][j] == ".":
        return "."
    adj_occupied = 0
    if 0 <= i-1:
        if 0 <= j-1:
            adj_occupied += 1 if seats[i-1][j-1] == "#" else 0
        adj_occupied += 1 if seats[i-1][j] == "#" else 0
        if j+1 < len(seats[i-1]):
            adj_occupied += 1 if seats[i-1][j+1] == "#" else 0
    if 0 <= j-1:
        adj_occupied += 1 if seats[i][j-1] == "#" else 0
    if j+1 < len(seats[i]):
        adj_occupied += 1 if seats[i][j+1] == "#" else 0
    if i+1 < len(seats):
        if 0 <= j-1:
            adj_occupied += 1 if seats[i+1][j-1] == "#" else 0
        adj_occupied += 1 if seats[i+1][j] == "#" else 0
        if j+1 < len(seats[i+1]):
            adj_occupied += 1 if seats[i+1][j+1] == "#" else 0
    if seats[i][j] == "L":
        if adj_occupied == 0:
            return "#"
        else:
            return "L"
    elif seats[i][j] == "#":
        if adj_occupied >= 4:
            return "L"
        else:
            return "#"


def updated_seat2(seats, i, j):
    if seats[i][j] == ".":
        return "."
    adj_occupied = 0

    # up-left
    off = 1
    while i - off >= 0 and j - off >= 0:
        if seats[i-off][j-off] == "#":
            adj_occupied += 1
            break
        elif seats[i-off][j-off] == "L":
            break
        off += 1

    # up
    off = 1
    while i - off >= 0:
        if seats[i-off][j] == "#":
            adj_occupied += 1
            break
        elif seats[i-off][j] == "L":
            break
        off += 1

    # up-right
    off = 1
    while i - off >= 0 and j + off < len(seats[i-off]):
        if seats[i-off][j+off] == "#":
            adj_occupied += 1
            break
        elif seats[i-off][j+off] == "L":
            break
        off += 1

    # left
    off = 1
    while j - off >= 0:
        if seats[i][j-off] == "#":
            adj_occupied += 1
            break
        elif seats[i][j-off] == "L":
            break
        off += 1

    # right
    off = 1
    while j + off < len(seats[i]):
        if seats[i][j+off] == "#":
            adj_occupied += 1
            break
        elif seats[i][j+off] == "L":
            break
        off += 1

    # down-left
    off = 1
    while i + off < len(seats) and j - off >= 0:
        if seats[i+off][j-off] == "#":
            adj_occupied += 1
            break
        elif seats[i+off][j-off] == "L":
            break
        off += 1

    # down
    off = 1
    while i + off < len(seats):
        if seats[i+off][j] == "#":
            adj_occupied += 1
            break
        elif seats[i+off][j] == "L":
            break
        off += 1

    # down-right
    off = 1
    while i + off < len(seats) and j + off < len(seats[i+off]):
        if seats[i+off][j+off] == "#":
            adj_occupied += 1
            break
        elif seats[i+off][j+off] == "L":
            break
        off += 1

    if seats[i][j] == "L":
        if adj_occupied == 0:
            return "#"
        else:
            return "L"
    elif seats[i][j] == "#":
        if adj_occupied >= 5:
            return "L"
        else:
            return "#"


def updated_seats_and_changes(seats, change_f):
    new_seats = []
    changes = 0
    for i in range(len(seats)):
        new_row = []
        for j in range(len(seats[i])):
            new_row.append(change_f(seats, i, j))
            if new_row[j] != seats[i][j]:
                changes += 1
        new_seats.append("".join(new_row))
    return (new_seats, changes)


def update_until_stable(seats, change_f):
    changes = 0
    i = 0
    while True:
        i += 1
        seats, changes = updated_seats_and_changes(seats, change_f)
        if changes == 0:
            break
    return (seats, i - 1)


def count_occupied(seats):
    return sum([1 if c == "#" else 0 for row in seats for c in row])


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        seats = fp.read().strip().splitlines()
    print("Part 1:")
    final_seats, _ = update_until_stable(seats, updated_seat)
    print(count_occupied(final_seats))
    print("Part 2:")
    final_seats2, _ = update_until_stable(seats, updated_seat2)
    print(count_occupied(final_seats2))
