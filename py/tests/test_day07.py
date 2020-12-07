from .context import advent_of_code_2020
from advent_of_code_2020.day07 import *


test_text = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
    """.strip()


def test_parse_rules():
    rules = parse_rules_list(test_text)
    assert len(rules) == 9
    assert rules["light red"] == {"bright white": 1, "muted yellow": 2}
    assert rules["dark orange"] == {"bright white": 3, "muted yellow": 4}
    assert rules["bright white"] == {"shiny gold": 1}
    assert rules["muted yellow"] == {"shiny gold": 2, "faded blue": 9}
    assert rules["shiny gold"] == {"dark olive": 1, "vibrant plum": 2}
    assert rules["dark olive"] == {"faded blue": 3, "dotted black": 4}
    assert rules["vibrant plum"] == {"faded blue": 5, "dotted black": 6}
    assert rules["faded blue"] == {}
    assert rules["dotted black"] == {}


def test_possible_containers():
    rules = parse_rules_list(test_text)
    rules2 = invert_rules(rules)
    assert possible_containers(rules2, "shiny gold") == \
        set(["bright white", "muted yellow", "dark orange", "light red"])


def test_bag_count():
    test_text2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
    """.strip()

    rules = parse_rules_list(test_text2)
    assert bag_count(rules, "dark violet") == 0
    assert bag_count(rules, "dark blue") == 2
    assert bag_count(rules, "shiny gold") == 126
