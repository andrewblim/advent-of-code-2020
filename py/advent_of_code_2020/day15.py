def initialize_tracking(initial):
    return (initial[-1], {x: i for i, x in enumerate(initial[0:-1])})


def update_tracking(prev_number, i, last_occ):
    if prev_number not in last_occ:
        next_number = 0
    else:
        next_number = i - 1 - last_occ[prev_number]
    last_occ[prev_number] = i - 1
    return next_number


def get_sequence(initial, n):
    if n <= len(initial):
        return initial[n-1]
    last_number, last_occ = initialize_tracking(initial)
    for i in range(len(initial), n):
        last_number = update_tracking(last_number, i, last_occ)
    return last_number


if __name__ == "__main__":
    print("Part 1:")
    x = get_sequence([17,1,3,16,19,0], 2020)
    print(x)
    print("Part 2:")
    x = get_sequence([17,1,3,16,19,0], 30000000)
    print(x)
