import sys


def transform(subject, loop_size=1, init=1, mod=20201227):
    value = init
    for i in range(loop_size):
        value = (value * subject) % mod
    return value


def find_loop_size(subject, key, init=1):
    loop_size = 0
    val = init
    while val != key:
        val = transform(subject=subject, init=val)
        loop_size += 1
    return loop_size


def find_encryption_key(key1, key2, subject):
    loop_size1 = find_loop_size(subject, key1)
    loop_size2 = find_loop_size(subject, key2)
    encryption1 = transform(key2, loop_size1)
    encryption2 = transform(key1, loop_size2)
    if encryption1 != encryption2:
        raise RuntimeError(f"unequal encryption keys {encryption1} {encryption2}")
    return encryption1


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = fp.read().strip()
    print("Part 1:")
    key1, key2 = [int(x) for x in input.splitlines()]
    print(find_encryption_key(key1, key2, subject=7))
    print("Part 2:")
