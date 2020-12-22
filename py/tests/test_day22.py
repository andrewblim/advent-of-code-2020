from .context import advent_of_code_2020
from advent_of_code_2020.day22 import *


def test_play_combat():
    test_input = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
    """.strip()
    deck1, deck2 = parse_decks(test_input)
    deck1, deck2 = play_combat(deck1, deck2)
    assert list(deck1) == []
    assert list(deck2) == [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]
    assert score_deck(deck1) == 0
    assert score_deck(deck2) == 306


def test_play_recursive_combat_noloop():
    test_input = """
Player 1:
43
19

Player 2:
2
29
14
    """.strip()
    deck1, deck2 = parse_decks(test_input)
    winner, final_deck1, final_deck2 = play_recursive_combat(deck1, deck2)
    assert winner == 1
    assert final_deck1 == deck1
    assert final_deck2 == deck2


def test_play_recursive_combat():
    test_input = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
    """.strip()
    deck1, deck2 = parse_decks(test_input)
    winner, final_deck1, final_deck2 = play_recursive_combat(deck1, deck2)
    assert winner == 2
    assert final_deck1 == []
    assert final_deck2 == [7, 5, 6, 2, 4, 1, 10, 8, 9, 3]
    assert score_deck(final_deck1) == 0
    assert score_deck(final_deck2) == 291
