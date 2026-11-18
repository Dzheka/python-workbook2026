import random


def create_deck():
    a = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    b = ['H', 'D', 'C', 'S']
    deck = []

    for i in b:
        for j in a:
            deck.append(j + i)

    return deck


def shuffle_deck(deck: list[str]):
    a = deck[:]
    random.shuffle(a)
    return a