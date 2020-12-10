import sys


def jolt_diffs_on_full_chain(adapters):
    adapters = [0] + adapters
    jolt_diffs = [0, 0, 0]
    for x, y in zip(adapters, adapters[1:]):
        jolt_diffs[y-x-1] += 1
    jolt_diffs[2] += 1  # device assumed 3 higher than max
    return jolt_diffs


def legal_chains(adapters):
    adapters = [0] + adapters
    ways = [0] * len(adapters)
    ways[0] = 1
    for i in range(1, len(ways)):
        for j in range(0, i):
            if adapters[j] >= adapters[i] - 3:
                ways[i] += ways[j]
    return ways[-1]



if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        adapters = [int(line.strip()) for line in fp.readlines()]
    adapters.sort()
    print("Part 1:")
    diffs = jolt_diffs_on_full_chain(adapters)
    print(diffs)
    print(diffs[0] * diffs[2])
    print("Part 2:")
    print(legal_chains(adapters))
