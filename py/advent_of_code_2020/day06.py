import sys
from functools import reduce


def parse_question_data(full_data):
    return [data.split("\n") for data in full_data.split("\n\n")]


def count_all_yeses(data):
    return len(set("".join(data)))


def count_all_yeses2(data):
    return len(reduce(lambda x, y: set(x) & set(y), data))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        question_data = fp.read().strip()
    print("Part 1:")
    parsed_data = parse_question_data(question_data)
    print(sum([count_all_yeses(x) for x in parsed_data]))
    print("Part 2:")
    print(sum([count_all_yeses2(x) for x in parsed_data]))
