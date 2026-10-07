import pytest

try:
    from gregorian_to_ordinal import gregorian_to_ordinal
except ImportError:
    gregorian_to_ordinal = None

pytestmark = pytest.mark.skipif(
    gregorian_to_ordinal is None, reason="gregorian_to_ordinal function not implemented"
)


@pytest.mark.parametrize(
    "year, month, day, expected",
    [
        (2024, 1, 1, 1),
        (2024, 2, 1, 32),
        (2024, 2, 29, 60),  # Leap year
        (2023, 3, 1, 60),  # Not leap year
        (2024, 12, 31, 366),
        (2023, 12, 31, 365),
        (2024, 4, 9, 100),
    ],
)
def test_gregorian_to_ordinal(year, month, day, expected):
    assert gregorian_to_ordinal(year, month, day) == expected
