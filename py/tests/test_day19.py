from .context import advent_of_code_2020
from advent_of_code_2020.day19 import *


rule_input1 = """
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
""".strip()

rule_input2 = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
""".strip()


def test_parse_rules():
    assert parse_rules(rule_input1.splitlines()) == {
        0: [[1,2]],
        1: "a",
        2: [[1,3], [3,1]],
        3: "b",
    }
    assert parse_rules(rule_input2.splitlines()) == {
        0: [[4,1,5]],
        1: [[2,3], [3,2]],
        2: [[4,4], [5,5]],
        3: [[4,5], [5,4]],
        4: "a",
        5: "b",
    }


def test_match_message():
    rules1 = parse_rules(rule_input1.splitlines())
    memo1 = {}
    assert match_message(3, "b", rules1, memo1)
    assert match_message(2, "ab", rules1, memo1)
    assert match_message(2, "ba", rules1, memo1)
    assert not match_message(2, "aa", rules1, memo1)
    assert match_message(0, "aab", rules1, memo1)
    assert match_message(0, "aba", rules1, memo1)
    assert not match_message(0, "bab", rules1, memo1)
    assert not match_message(0, "aaa", rules1, memo1)

    rules2 = parse_rules(rule_input2.splitlines())
    memo2 = {}
    for x in ["aaaabb", "aaabab", "abbabb", "abbbab",
              "aabaab", "aabbbb", "abaaab", "ababbb"]:
        assert match_message(0, x, rules2, memo2)

    matches = [match_message(0, x, rules2, memo2)
               for x in ["ababbb", "bababa", "abbbab", "aaabbb", "aaaabbb"]]
    assert matches == [True, False, True, False, False]


full_input = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".strip()


def test_match_message_with_loops():
    rules_text, test_text = full_input.split("\n\n")
    rules = parse_rules(rules_text.splitlines())
    memo = {}
    matches = [match_message(0, x, rules, memo) for x in test_text.splitlines()]
    assert matches == [False, True, False, False, False, False, True, True,
                       False, False, False, False, False, False, False]
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    memo = {}
    matches = [match_message(0, x, rules, memo) for x in test_text.splitlines()]
    assert matches == [False, True, True, True, True, True, True, True,
                       True, True, True, False, True, False, True]
