from random import choice
from random import randrange
def create_deck() -> list[str]:
    result  = []
    for i in 'HDCS':
        for j in range(2, 11):
            result.append(f"{j}{i}")
        for z in 'JQKA':
            result.append(f'{z}{i}')
    return result

def shuffle_deck(deck: list[str]) -> list[str]:
    deck = deck.copy()
    length = len(deck)
    # I ll just swap random items multiple times
    for i in range(0, length):
        a = randrange(0, length)
        b = randrange(0, length)
        temp = deck[a]
        deck[a] = deck[b]
        deck[b] = temp
    return deck


if __name__ == "__main__":
    # Test your functions
    deck = create_deck()
    print(f"Deck size: {len(deck)}")  # 52
    print(f"First 5 cards: {deck[:5]}")

    shuffled = shuffle_deck(deck)
    print(f"Shuffled first 5: {shuffled[:5]}")