import sys


def initial_board(input):
    board = {}
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                board[(x, y, 0)] = True
    return board


def bounding_box(board):
    coords = list(zip(*board.keys()))
    return list(zip(map(min, coords), map(max, coords)))


def neighbors(x, y, z):
    return [(a, b, c)
            for a in range(x-1, x+2)
            for b in range(y-1, y+2)
            for c in range(z-1, z+2)
            if (a, b, c) != (x, y, z)]


def updated_board(board):
    x_bounds, y_bounds, z_bounds = bounding_box(board)
    new_board = {}
    for x in range(x_bounds[0] - 1, x_bounds[1] + 2):
        for y in range(y_bounds[0] - 1, y_bounds[1] + 2):
            for z in range(z_bounds[0] - 1, z_bounds[1] + 2):
                active_neighbors = sum([1 for p in neighbors(x, y, z) if p in board])
                if (x, y, z) in board and active_neighbors == 2 or active_neighbors == 3:
                    new_board[(x, y, z)] = True
                elif (x, y, z) not in board and active_neighbors == 3:
                    new_board[(x, y, z)] = True
    return new_board


def initial_board2(input):
    board = {}
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                board[(x, y, 0, 0)] = True
    return board


def neighbors2(x, y, z, w):
    return [(a, b, c, d)
            for a in range(x-1, x+2)
            for b in range(y-1, y+2)
            for c in range(z-1, z+2)
            for d in range(w-1, w+2)
            if (a, b, c, d) != (x, y, z, w)]


def updated_board2(board):
    x_bounds, y_bounds, z_bounds, w_bounds = bounding_box(board)
    new_board = {}
    for x in range(x_bounds[0] - 1, x_bounds[1] + 2):
        for y in range(y_bounds[0] - 1, y_bounds[1] + 2):
            for z in range(z_bounds[0] - 1, z_bounds[1] + 2):
                for w in range(w_bounds[0] - 1, w_bounds[1] + 2):
                    active_neighbors = sum([1 for p in neighbors2(x, y, z, w) if p in board])
                    if (x, y, z, w) in board and active_neighbors == 2 or active_neighbors == 3:
                        new_board[(x, y, z, w)] = True
                    elif (x, y, z) not in board and active_neighbors == 3:
                        new_board[(x, y, z, w)] = True
    return new_board


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = fp.read().strip()
    print("Part 1:")
    board = initial_board(input)
    for i in range(6):
        board = updated_board(board)
    print(len(board.keys()))
    print("Part 2:")
    board = initial_board2(input)
    for i in range(6):
        board = updated_board2(board)
    print(len(board.keys()))
