import sys
from collections import deque


def parse_decks(input):
    deck1, deck2 = input.split("\n\n")
    deck1 = [int(x) for x in deck1.split("\n")[1:]]
    deck2 = [int(x) for x in deck2.split("\n")[1:]]
    return (deck1, deck2)


def play_combat(deck1, deck2):
    deck1 = deque(deck1)
    deck2 = deque(deck2)
    while len(deck1) > 0 and len(deck2) > 0:
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    return (deck1, deck2)


def score_deck(deck):
    score = 0
    for i, x in enumerate(deck):
        score += (len(deck) - i) * x
    return score


def str_deck(deck):
    return ",".join([str(x) for x in deck])


def play_recursive_combat(deck1, deck2):
    deck1 = deque(deck1)
    deck2 = deque(deck2)
    prev_seen = set()
    while len(deck1) > 0 and len(deck2) > 0:
        if str_deck(deck1) in prev_seen:
            # early instant win player 1
            return (1, list(deck1), list(deck2))
        prev_seen.add(str_deck(deck1))
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > len(deck1) or card2 > len(deck2):
            # regular combat
            if card1 > card2:
                winner = 1
            else:
                winner = 2
        else:
            # recursive combat
            subdeck1 = deque(list(deck1)[0:card1])
            subdeck2 = deque(list(deck2)[0:card2])
            result = play_recursive_combat(subdeck1, subdeck2)
            winner = result[0]
        if winner == 1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    if len(deck1) == 0:
        return (2, list(deck1), list(deck2))
    else:
        return (1, list(deck1), list(deck2))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = fp.read().strip()
    print("Part 1:")
    deck1, deck2 = parse_decks(input)
    final_deck1, final_deck2 = play_combat(deck1, deck2)
    print(score_deck(final_deck1))
    print(score_deck(final_deck2))
    print("Part 2:")
    winner, final_deck1, final_deck2 = play_recursive_combat(deck1, deck2)
    print(winner)
    print(score_deck(final_deck1))
    print(score_deck(final_deck2))
