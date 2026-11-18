from random import choice

def deal_hands(deck: list[str], num_players: int, cards_per_player: int) -> list[list[str]]:
    result = []
    for i in range(num_players):
        hand = []
        for j in range(cards_per_player):
            card = deck.pop(0)
            hand.append(card)

        result.append(hand)
    return result


if __name__ == "__main__":
    # Test your function
    deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H']
    hands = deal_hands(deck, 3, 3)
    for i, hand in enumerate(hands, 1):
        print(f"Player {i}: {hand}")
    # Player 1: ['2H', '3H', '4H']
    # Player 2: ['5H', '6H', '7H']
    # Player 3: ['8H', '9H', '10H']