def deal_hands(deck: list[str], num_players: int, cards_per_player: int) -> list[list[str]]:
    if num_players * cards_per_player > len(deck):
        raise ValueError("Not enough cards in deck")

    hands = []
    for i in range(num_players):
        start = i * cards_per_player
        end = start + cards_per_player
        hands.append(deck[start:end])
    return hands