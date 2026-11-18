def deal_hands(deck: list[str], num_players: int, cards_per_player: int):
    a = []

    for i in range(num_players):
        start = i * cards_per_player
        hand = deck[start:start + cards_per_player]
        a.append(hand)

    return a
