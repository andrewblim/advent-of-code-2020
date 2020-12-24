import sys


def parse_moves(input):
    moves = []
    i = 0
    while i < len(input):
        if input[i] in ["e", "w"]:
            moves.append(input[i])
            i += 1
        elif input[i] in ["n", "s"]:
            moves.append(input[i:i+2])
            i += 2
    return moves


def move_to_tile(moves, start=(0,0)):
    cur = start
    for move in moves:
        if move == "e":
            cur = (cur[0] + 2, cur[1])
        elif move == "w":
            cur = (cur[0] - 2, cur[1])
        elif move == "ne":
            cur = (cur[0] + 1, cur[1] + 1)
        elif move == "nw":
            cur = (cur[0] - 1, cur[1] + 1)
        elif move == "se":
            cur = (cur[0] + 1, cur[1] - 1)
        elif move == "sw":
            cur = (cur[0] - 1, cur[1] - 1)
        else:
            raise RuntimeError(f"unrecognized move {move}")
    return cur


def flip_tiles(moves_list):
    flipped = set()
    for moves in moves_list:
        x = move_to_tile(moves)
        if x in flipped:
            flipped.remove(x)
        else:
            flipped.add(x)
    return flipped


def flip_tiles_daily(flipped):
    new_flipped = set()
    visited_unflipped = set()
    for tile in flipped:
        neighbors = [
            move_to_tile(["e"], tile),
            move_to_tile(["w"], tile),
            move_to_tile(["ne"], tile),
            move_to_tile(["nw"], tile),
            move_to_tile(["se"], tile),
            move_to_tile(["sw"], tile),
        ]
        flipped_neighbors = sum([x in flipped for x in neighbors])
        if 1 <= flipped_neighbors <= 2:
            new_flipped.add(tile)
        for neighbor in neighbors:
            if neighbor not in visited_unflipped:
                neighbor_neighbors = [
                    move_to_tile(["e"], neighbor),
                    move_to_tile(["w"], neighbor),
                    move_to_tile(["ne"], neighbor),
                    move_to_tile(["nw"], neighbor),
                    move_to_tile(["se"], neighbor),
                    move_to_tile(["sw"], neighbor),
                ]
                flipped_neighbor_neighbors = sum([x in flipped for x in neighbor_neighbors])
                if flipped_neighbor_neighbors == 2:
                    new_flipped.add(neighbor)
                visited_unflipped.add(neighbor)
    return new_flipped


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = fp.read().strip()
    print("Part 1:")
    moves_list = [parse_moves(line) for line in input.splitlines()]
    flipped = flip_tiles(moves_list)
    print(len(flipped))
    print("Part 2:")
    for i in range(100):
        flipped = flip_tiles_daily(flipped)
    print(len(flipped))
