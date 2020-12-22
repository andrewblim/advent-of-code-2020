from .context import advent_of_code_2020
from advent_of_code_2020.day21 import *


def test_allergens():
    test_input = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
    """.strip()
    foods = [parse_foods(line) for line in test_input.splitlines()]
    content = possible_allergen_content(foods)
    assert allergen_free_ingredients(foods, content) == \
        {"kfcds", "nhms", "sbzzf", "trh"}

    pairings = determine_allergens(content)
    assert pairings == [
        ("dairy", "mxmxvkd"),
        ("fish", "sqjhc"),
        ("soy", "fvjkl"),
    ]
