from .context import advent_of_code_2020
from advent_of_code_2020.day18 import *


def test_eval_expr():
    assert eval_expr("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert eval_expr("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert eval_expr("2 * 3 + (4 * 5)") == 26
    assert eval_expr("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert eval_expr("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert eval_expr("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632


def test_eval_expr2():
    assert eval_expr2("1 + 2 * 3 + 4 * 5 + 6") == 231
    assert eval_expr2("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert eval_expr2("2 * 3 + (4 * 5)") == 46
    assert eval_expr2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert eval_expr2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert eval_expr2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340
