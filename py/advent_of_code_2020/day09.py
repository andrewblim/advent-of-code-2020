import sys
from itertools import combinations


def check_xmas_code(code, n):
    queue = [x[0] + x[1] for x in combinations(code[:n], 2)]
    for i, x in enumerate(code[n:]):
        if x not in queue:
            return x
        j = 0
        for k in range(n-1, 0, -1):
            # shift the numbers over so that each time, the first n-1
            # entries have code[0] + code[1], ..., code[n-1], then
            # the next have code[1] + code[2], ..., code[n-1], etc.
            queue[j:(j+k-1)] = queue[(j+k):(j+2*k-1)]
            queue[j+k-1] = code[i+n-k] + x
            j += k


def find_contiguous_sum(code, target):
    partial_sums = list(code)
    for offset in range(1, len(code)):
        # print(f"Offset: {offset}")
        # first pass: add code[1] to ps[0], code[2] to ps[1], ..., code[n] to ps[n-1], drop ps[n]
        # second pass: add code[2] to ps[0], code[3] to ps[1], ..., code[n] to ps[n-2], drop ps[n-1]
        # ...
        # until: add code[n-1] to ps[0], drop ps[1]
        new_partial_sums = []
        for start in range(0, len(code) - offset):
            # print(f"Start: {start}")
            x = partial_sums[start] + code[start + offset]
            if x == target:
                return (start, start + offset)
            new_partial_sums.append(x)
        partial_sums = new_partial_sums


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        code = [int(line.strip()) for line in fp.readlines()]
    print("Part 1:")
    invalid = check_xmas_code(code, 25)
    print(invalid)
    print("Part 2:")
    start, end = find_contiguous_sum(code, invalid)
    subrange = code[start:(end+1)]
    print((min(subrange), max(subrange)))
    print(min(subrange) + max(subrange))
