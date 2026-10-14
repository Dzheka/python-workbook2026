import pytest

try:
    from deck_operations import create_deck, shuffle_deck
except ImportError:
    create_deck = None
    shuffle_deck = None


@pytest.mark.skipif(create_deck is None, reason="create_deck function not implemented")
def test_create_deck():
    deck = create_deck()
    assert len(deck) == 52
    assert "2H" in deck
    assert "AS" in deck
    assert "KD" in deck
    assert len(set(deck)) == 52


@pytest.mark.skipif(
    shuffle_deck is None, reason="shuffle_deck function not implemented"
)
def test_shuffle_deck():
    deck = create_deck()
    shuffled = shuffle_deck(deck)

    assert len(shuffled) == 52
    assert set(shuffled) == set(deck)

    # The original deck should not be modified
    deck2 = create_deck()
    assert deck == deck2
