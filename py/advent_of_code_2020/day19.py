import sys
import re


def parse_rules(input):
    rules = {}
    for rule_text in input:
        rule_no, cond = rule_text.split(": ")
        rule_no = int(rule_no)
        if re.match(r'^"."$', cond):
            rules[rule_no] = cond[1]
        else:
            subcond = cond.split(" | ")
            rules[rule_no] = [[int(y) for y in x.split(" ")] for x in subcond]
    return rules


def match_message(rule, x, rules, memo):
    # rule can be a string (direct match), an integer (looks up the rule),
    # or a list of lists of strings/integers (matches any of them)
    if isinstance(rule, str):
        return rule == x
    if isinstance(rule, int):
        if (rule, x) not in memo:
            memo[(rule, x)] = match_message(rules[rule], x, rules, memo)
        return memo[(rule, x)]
    for subrule in rule:
        if len(subrule) == 0:
            return x == ""
        for i in range(0, len(x)+1):
            match = match_message(subrule[0], x[:i], rules, memo) and \
                    match_message([subrule[1:]], x[i:], rules, memo)
            if match:
                return True
    return False


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = fp.read().strip()
    print("Part 1:")
    rules_text, test_text = input.split("\n\n")
    rules = parse_rules(rules_text.splitlines())
    test_text = test_text.splitlines()
    memo = {}
    matches = 0
    for i, x in enumerate(test_text):
        if i % 25 == 0:
            print(f"On {i}/{len(test_text)}")
        if match_message(0, x, rules, memo):
            matches += 1
    print(matches)
    print("Part 2:")
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    memo = {}
    matches = 0
    for i, x in enumerate(test_text):
        if i % 25 == 0:
            print(f"On {i}/{len(test_text)}")
        if match_message(0, x, rules, memo):
            matches += 1
    print(matches)
