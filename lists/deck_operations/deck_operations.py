import random


def create_deck() -> list[str]:
    suits = ["H", "D", "C", "S"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    return [f"{rank}{suit}" for suit in suits for rank in ranks]


def shuffle_deck(deck: list[str]) -> list[str]:
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled
