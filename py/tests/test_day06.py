from .context import advent_of_code_2020
from advent_of_code_2020.day06 import *


def test_yeses():
    test_data = """
abc

a
b
c

ab
ac

a
a
a
a

b
    """.strip()
    parsed_data = parse_question_data(test_data)
    assert [count_all_yeses(x) for x in parsed_data] == [3, 3, 3, 1, 1]
    assert [count_all_yeses2(x) for x in parsed_data] == [3, 0, 1, 1, 1]
