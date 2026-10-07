import pytest

try:
    from normalize_fraction import normalize_fraction
except ImportError:
    normalize_fraction = None

pytestmark = pytest.mark.skipif(
    normalize_fraction is None, reason="normalize_fraction function not implemented"
)


@pytest.mark.parametrize(
    "numerator, denominator, expected",
    [
        (4, 8, (1, 2)),
        (6, 9, (2, 3)),
        (5, 10, (1, 2)),
        (7, 3, (7, 3)),
        (0, 5, (0, 1)),
        (12, 16, (3, 4)),
        (100, 25, (4, 1)),
        (17, 19, (17, 19)),
    ],
)
def test_normalize_fraction(numerator, denominator, expected):
    assert normalize_fraction(numerator, denominator) == expected
