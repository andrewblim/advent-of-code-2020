import sys
import itertools


def find_sum_pair(vals, target):
    for x, y in itertools.combinations(vals, r=2):
        if x + y == target:
            return x, y


def find_sum_triplet(vals, target):
    for x, y, z in itertools.combinations(vals, r=3):
        if x + y + z == target:
            return x, y, z


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = [int(line.rstrip()) for line in fp.readlines()]
    print("Part 1:")
    x = find_sum_pair(input, 2020)
    print(x)
    print(x[0] * x[1])
    print("Part 2:")
    x = find_sum_triplet(input, 2020)
    print(x)
    print(x[0] * x[1] * x[2])
