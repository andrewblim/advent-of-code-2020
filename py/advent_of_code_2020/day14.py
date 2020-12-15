import sys
import re


def parse_instruction(instruction):
    if instruction[0:7] == "mask = ":
        m1 = int("".join(["1" if x == "X" else "0" for x in instruction[7:]]), 2)
        m2 = int("".join(["0" if x == "X" else x for x in instruction[7:]]), 2)
        return ("mask", m1, m2)
    else:
        x = re.match(r"mem\[(\d+)\] = (\d+)", instruction)
        return ("mem", int(x[1]), int(x[2]))


def masked_value(x, m1, m2):
    return (x & m1) ^ m2


def parse_instructions(instructions):
    memory = {}
    mask = (0, 0)
    for instruction in instructions:
        type, v1, v2 = parse_instruction(instruction)
        if type == "mask":
            mask = (v1, v2)
        else:
            memory[v1] = masked_value(v2, *mask)
    return memory


def masked_values2(x, m1, m2):
    base_value = (x | m2) & (~m1)
    values = [base_value]
    i = 0
    while m1 > 0:
        if m1 % 2 == 1:
            values.extend([v + 2**i for v in values])
        i += 1
        m1 >>= 1
    return values


def parse_instructions2(instructions):
    memory = {}
    mask = (0, 0)
    for instruction in instructions:
        type, v1, v2 = parse_instruction(instruction)
        if type == "mask":
            mask = (v1, v2)
        else:
            for value in masked_values2(v1, *mask):
                memory[value] = v2
    return memory


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        instructions = [x.strip() for x in fp.readlines()]
    print("Part 1:")
    memory = parse_instructions(instructions)
    print(sum(memory.values()))
    print("Part 2:")
    memory2 = parse_instructions2(instructions)
    print(sum(memory2.values()))
