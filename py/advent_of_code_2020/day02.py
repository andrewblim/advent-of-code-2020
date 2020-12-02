import sys
import re


def read_policy_and_password(input):
    x = re.match(r"(\d+)-(\d+) (\w)\: (\w+)", input)
    return (int(x[1]), int(x[2]), x[3], x[4])


def validate_password_against_policy(password, letter, lower, upper):
    n = len([c for c in password if c == letter])
    return lower <= n <= upper


def validate_policy_and_password(input):
    lower, upper, letter, password = read_policy_and_password(input)
    return validate_password_against_policy(password, letter, lower, upper)


def validate_password_against_policy2(password, letter, p1, p2):
    return (p1 <= len(password) and password[p1-1] == letter) ^ \
           (p2 <= len(password) and password[p2-1] == letter)


def validate_policy_and_password2(input):
    p1, p2, letter, password = read_policy_and_password(input)
    return validate_password_against_policy2(password, letter, p1, p2)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = [line.rstrip() for line in fp.readlines()]
    print("Part 1:")
    n = len([x for x in input if validate_policy_and_password(x)])
    print(n)
    print("Part 2:")
    n = len([x for x in input if validate_policy_and_password2(x)])
    print(n)
