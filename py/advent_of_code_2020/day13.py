import sys
import math


def parse_input(input):
    ready, buses = input.split("\n")
    return (int(ready), buses.split(","))


def earliest_bus_possible_info(ready, buses):
    buses = [int(bus) for bus in buses if bus != "x"]
    bus = min(buses, key=lambda x: math.ceil(ready / x) * x - ready)
    depart = math.ceil(ready / bus) * bus
    return (bus, depart)


def find_earliest_timestamp(buses):
    cur = 0
    inc = 1
    indexed_buses = [(i, int(bus)) for (i, bus) in enumerate(buses) if bus != "x"]
    for i, bus in indexed_buses:
        target = (bus - i) % bus
        while cur % bus != target:
            cur += inc
        inc = lcm(inc, bus)
    return cur


def lcm(x, y):
    return int(x * y / gcd(x, y))


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        ready, buses = parse_input(fp.read().strip())
    print("Part 1:")
    bus, depart = earliest_bus_possible_info(ready, buses)
    print((bus, depart))
    print((depart - ready) * bus)
    print("Part 2:")
    print(find_earliest_timestamp(buses))
