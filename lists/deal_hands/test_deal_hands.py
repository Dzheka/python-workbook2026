import pytest

try:
    from deal_hands import deal_hands
except ImportError:
    deal_hands = None

pytestmark = pytest.mark.skipif(
    deal_hands is None, reason="deal_hands function not implemented"
)


@pytest.mark.parametrize(
    "deck, num_players, cards_per_player, expected",
    [
        (
            ["1", "2", "3", "4"],
            2,
            2,
            [["1", "2"], ["3", "4"]],
        ),
        (
            ["2H", "3H", "4H", "5H", "6H", "7H"],
            2,
            3,
            [["2H", "3H", "4H"], ["5H", "6H", "7H"]],
        ),
        (
            ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            3,
            3,
            [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
        ),
    ],
)
def test_deal_hands(deck, num_players, cards_per_player, expected):
    assert deal_hands(deck, num_players, cards_per_player) == expected
