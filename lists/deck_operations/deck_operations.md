# Deck Operations

Create and shuffle a deck of playing cards.

## Task

- Create a function `create_deck()` that generates a standard 52-card deck
- Create a function `shuffle_deck(deck)` that shuffles the deck

## Cards

A card is its rank followed by its suit, e.g. `"2H"`, `"AS"`, `"KD"`.

- Ranks (13): `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `J`, `Q`, `K`, `A`
- Suits (4): `H` (Hearts), `D` (Diamonds), `C` (Clubs), `S` (Spades)

## Template:

```python
def create_deck() -> list[str]:
    pass


def shuffle_deck(deck: list[str]) -> list[str]:
    pass


if __name__ == "__main__":
    # Test your functions
    deck = create_deck()
    print(f"Deck size: {len(deck)}")  # 52
    print(f"First 5 cards: {deck[:5]}")

    shuffled = shuffle_deck(deck)
    print(f"Shuffled first 5: {shuffled[:5]}")
```

