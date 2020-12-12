import sys
import math


def parse_move(desc):
    return (desc[0], int(desc[1:]))


def update_position(cur, move):
    x, y, theta = cur
    dir, chg = move
    if dir == "N":
        return (x, y + chg, theta)
    elif dir == "S":
        return (x, y - chg, theta)
    elif dir == "E":
        return (x + chg, y, theta)
    elif dir == "W":
        return (x - chg, y, theta)
    elif dir == "F":
        rad = math.radians(theta)
        return (x + chg * math.cos(rad), y + chg * math.sin(rad), theta)
    elif dir == "R":
        return (x, y, (theta - chg) % 360)
    elif dir == "L":
        return (x, y, (theta + chg) % 360)
    else:
        raise RuntimeError(f"unrecognized direction {dir}")


def update_position2(cur, move):
    # wx, wy are relative to x, y, not absolute
    x, y, wx, wy = cur
    dir, chg = move
    if dir == "N":
        return (x, y, wx, wy + chg)
    elif dir == "S":
        return (x, y, wx, wy - chg)
    elif dir == "E":
        return (x, y, wx + chg, wy)
    elif dir == "W":
        return (x, y, wx - chg, wy)
    elif dir == "F":
        return (x + chg * wx, y + chg * wy, wx, wy)
    elif dir == "R":
        theta = -math.radians(chg)
        return (x, y,
                wx * math.cos(theta) - wy * math.sin(theta),
                wx * math.sin(theta) + wy * math.cos(theta))
    elif dir == "L":
        theta = math.radians(chg)
        return (x, y,
                wx * math.cos(theta) - wy * math.sin(theta),
                wx * math.sin(theta) + wy * math.cos(theta))
    else:
        raise RuntimeError(f"unrecognized direction {dir}")


def update_position_after_moves(cur, moves, f):
    for move in moves:
        cur = f(cur, move)
    return cur


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        moves = [parse_move(line.strip()) for line in fp.readlines()]
    print("Part 1:")
    pos = update_position_after_moves((0, 0, 0), moves, update_position)
    print(pos)
    print(abs(pos[0]) + abs(pos[1]))
    print("Part 2:")
    pos = update_position_after_moves((0, 0, 10, 1), moves, update_position2)
    print(pos)
    print(abs(pos[0]) + abs(pos[1]))
