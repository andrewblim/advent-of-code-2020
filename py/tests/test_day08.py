from .context import advent_of_code_2020
from advent_of_code_2020.day08 import *


test_text = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()

instructions = [parse_instruction(line.strip()) for line in test_text.splitlines()]

def test_execute_instructions():
    assert execute_instructions(instructions) == \
        ({0: 1, 1: 2, 2: 3, 3: 6, 4: 7, 6: 4, 7: 5}, 5, 1)

def test_fix_jmp_instruction():
    assert fix_jmp_instruction(instructions) == (7, 8)
