import sys
import re


def parse_passport_data(full_data):
    return [dict([x.split(":") for line in data.split("\n") for x in line.split(" ")])
            for data in full_data.split("\n\n")]


def validate_passport(fields):
    return all(map(lambda x: x in fields,
                   ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]))


def validate_passport2(fields):
    try:
        if not re.match(r"^\d\d\d\d$", fields["byr"]):
            return False
        byr = int(fields["byr"])
        if byr < 1920 or byr > 2002:
            return False
        if not re.match(r"^\d\d\d\d$", fields["iyr"]):
            return False
        iyr = int(fields["iyr"])
        if iyr < 2010 or iyr > 2020:
            return False
        if not re.match(r"^\d\d\d\d$", fields["eyr"]):
            return False
        eyr = int(fields["eyr"])
        if eyr < 2020 or eyr > 2030:
            return False
        if not re.match(r"^\d+(cm|in)$", fields["hgt"]):
            return False
        hgt = int(fields["hgt"][:-2])
        hgt_unit = fields["hgt"][-2:]
        if hgt_unit == "cm" and (hgt < 150 or hgt > 193):
            return False
        elif hgt_unit == "in" and (hgt < 59 or hgt > 76):
            return False
        if not re.match(r"^#([0-9]|[a-f]){6}$", fields["hcl"]):
            return False
        if not fields["ecl"] in "amb blu brn gry grn hzl oth".split(" "):
            return False
        if not re.match(r"^([0-9]){9}$", fields["pid"]):
            return False
    except KeyError:
        return False
    return True


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        passport_data = fp.read().strip()
    print("Part 1:")
    data = parse_passport_data(passport_data)
    valid = [validate_passport(x) for x in data]
    print(sum(valid))
    print("Part 2:")
    data = parse_passport_data(passport_data)
    valid = [validate_passport2(x) for x in data]
    print(sum(valid))
