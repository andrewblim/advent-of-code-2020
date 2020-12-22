import sys
import re
from functools import reduce


def parse_foods(input):
    x = re.match(r"^(.+) \(contains (.+)\)", input)
    ingredients = x[1].split(" ")
    allergens = x[2].split(", ")
    return (ingredients, allergens)


def possible_allergen_content(foods):
    content = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen not in content:
                content[allergen] = set(ingredients)
            else:
                content[allergen] &= set(ingredients)
    return content


def allergen_free_ingredients(foods, content):
    ingredients = reduce(lambda x, y: x | y, [set(a[0]) for a in foods])
    ingredients_allergens = reduce(lambda x, y: x | y, [a for a in content.values()])
    return ingredients - ingredients_allergens


def determine_allergens(content):
    content = dict(content)
    pairings = []  # (allergen, ingredient)
    while len(content) > 0:
        definite = [(k, v.pop()) for k, v in content.items() if len(v) == 1]
        if len(definite) == 0:
            raise RuntimeError("Could not determine all allergens")
        pairings.extend(definite)
        definite_allergens, definite_ingredients = list(zip(*definite))
        for allergen in definite_allergens:
            del content[allergen]
        for k in content:
            content[k] -= set(definite_ingredients)
    return sorted(pairings)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = fp.read().strip()
    print("Part 1:")
    foods = [parse_foods(line) for line in input.splitlines()]
    content = possible_allergen_content(foods)
    allergen_free = allergen_free_ingredients(foods, content)
    all_ingredients = [y for x in foods for y in x[0]]
    print(sum([x in allergen_free for x in all_ingredients]))
    print("Part 2:")
    pairings = determine_allergens(content)
    print(",".join([x[1] for x in pairings]))
