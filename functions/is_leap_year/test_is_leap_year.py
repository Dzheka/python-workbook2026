import pytest

try:
    from is_leap_year import is_leap_year
except ImportError:
    is_leap_year = None

pytestmark = pytest.mark.skipif(
    is_leap_year is None, reason="is_leap_year function not implemented"
)


@pytest.mark.parametrize(
    "year, expected",
    [
        (1600, True),
        (1700, False),
        (1800, False),
        (1900, False),
        (2000, True),
        (2001, False),
        (2004, True),
        (2020, True),
        (2024, True),
        (2100, False),
    ],
)
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected
