import sys


def parse_instruction(line):
    op, arg = line.split(" ")
    return op, int(arg)  # works with + sign!


def execute_instructions(instructions, start_pos=0, start_acc=0):
    pos = start_pos
    acc = start_acc
    first_visit = {}
    step = 0
    while pos not in first_visit and pos < len(instructions):
        step += 1
        first_visit[pos] = step
        op, arg = instructions[pos]
        if op == "acc":
            acc += arg
            pos += 1
        elif op == "jmp":
            pos += arg
        elif op == "nop":
            pos += 1
        else:
            raise RuntimeError(f"unrecognized op {op}")
    if pos == len(instructions):
        return first_visit, acc, 0
    elif pos < len(instructions):
        return first_visit, acc, 1
    else:
        return first_visit, acc, 2


def fix_jmp_instruction(instructions):
    for i, (op, arg) in enumerate(instructions):
        if op == "jmp":
            new_instructions = list(instructions)
            new_instructions[i] = ("nop", arg)
            _, acc, exit_code = execute_instructions(new_instructions)
            if exit_code == 0:
                return i, acc
    raise RuntimeError("could not fix program")


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        instructions = [parse_instruction(line.strip())
                        for line in fp.readlines()]
    print("Part 1:")
    _, acc, _ = execute_instructions(instructions)
    print(acc)
    print("Part 2:")
    _, acc = fix_jmp_instruction(instructions)
    print(acc)
