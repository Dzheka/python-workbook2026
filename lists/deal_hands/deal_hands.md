# Deal Hands

Deal cards from a deck to multiple players.

## Task

- Create a function `deal_hands(deck, num_players, cards_per_player)`
- Return a list of hands, where each hand is a list of cards
- Each player receives the specified number of cards from the deck
- Assume the deck has enough cards: `len(deck) >= num_players * cards_per_player`

## Template:

```python
def deal_hands(deck: list[str], num_players: int, cards_per_player: int) -> list[list[str]]:
    pass


if __name__ == "__main__":
    # Test your function
    deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H']
    hands = deal_hands(deck, 3, 3)
    for i, hand in enumerate(hands, 1):
        print(f"Player {i}: {hand}")
    # Player 1: ['2H', '3H', '4H']
    # Player 2: ['5H', '6H', '7H']
    # Player 3: ['8H', '9H', '10H']
```

