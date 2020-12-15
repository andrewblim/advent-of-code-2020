from .context import advent_of_code_2020
from advent_of_code_2020.day14 import *


def test_masked_value():
    instruction = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    type, m1, m2 = parse_instruction(instruction)
    assert type == "mask"
    assert masked_value(11, m1, m2) == 73
    assert masked_value(101, m1, m2) == 101
    assert masked_value(0, m1, m2) == 64


def test_parse_instructions():
    instructions = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
    """.strip().splitlines()
    assert parse_instructions(instructions) == {7: 101, 8: 64}


def test_masked_values2():
    instruction = "mask = 000000000000000000000000000000X1001X"
    type, m1, m2 = parse_instruction(instruction)
    assert masked_values2(42, m1, m2) == [26, 27, 58, 59]
    instruction = "mask = 00000000000000000000000000000000X0XX"
    type, m1, m2 = parse_instruction(instruction)
    assert masked_values2(26, m1, m2) == [16, 17, 18, 19, 24, 25, 26, 27]


def test_parse_instructions2():
    instructions = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
    """.strip().splitlines()
    assert parse_instructions2(instructions) == {
        16: 1,
        17: 1,
        18: 1,
        19: 1,
        24: 1,
        25: 1,
        26: 1,
        27: 1,
        58: 100,
        59: 100,
    }
