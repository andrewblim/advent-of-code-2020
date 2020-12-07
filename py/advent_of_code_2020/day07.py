import sys
import re


def parse_rule(text):
    x = re.match(r"^(.+) bags contain (no other bags|.+)\.$", text)
    bag = x[1]
    contents = {}
    if x[2] != "no other bags":
        for bag_text in x[2].split(", "):
            y = re.match(r"^(\d+) (.+) bags?$", bag_text)
            contents[y[2]] = int(y[1])
    return {bag: contents}


def parse_rules_list(text):
    rules = {}
    for rule_text in text.splitlines():
        rules.update(parse_rule(rule_text))
    return rules


def invert_rules(rules):
    inverted_rules = {bag: {} for bag in rules.keys()}
    for bag1, contents in rules.items():
        for bag2, n in contents.items():
            if bag2 not in inverted_rules:
                inverted_rules[bag2] = {}
            if bag1 in inverted_rules[bag2]:
                raise KeyError(f"duplicate key {bag2}, {bag1}")
            inverted_rules[bag2][bag1] = n
    return inverted_rules


def possible_containers(rules, target):
    visited = set()
    frontier = [target]
    while len(frontier) > 0:
        visited |= set(frontier)
        frontier = [y for x in frontier for y in rules[x].keys()
                    if y not in visited]
    return visited - set([target])  # we're ignoring the target itself


def bag_count(rules, node):
    # assuming no cycles
    return sum([(bag_count(rules, k) + 1) * v for k, v in rules[node].items()])


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        rules_text = fp.read().strip()
    print("Part 1:")
    rules = parse_rules_list(rules_text)
    rules2 = invert_rules(rules)
    possibs = possible_containers(rules2, "shiny gold")
    print(len(possibs))
    print("Part 2:")
    print(bag_count(rules, "shiny gold"))
