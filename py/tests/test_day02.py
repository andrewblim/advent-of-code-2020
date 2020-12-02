from .context import advent_of_code_2020
from advent_of_code_2020.day02 import *


def test_validate_policy_and_password():
    assert validate_policy_and_password("1-3 a: abcde")
    assert not validate_policy_and_password("1-3 b: cdefg")
    assert validate_policy_and_password("2-9 c: ccccccccc")


def test_validate_policy_and_password2():
    assert validate_policy_and_password2("1-3 a: abcde")
    assert not validate_policy_and_password2("1-3 b: cdefg")
    assert not validate_policy_and_password2("2-9 c: ccccccccc")
