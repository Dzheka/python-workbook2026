import pytest

try:
    from ordinal_to_gregorian import ordinal_to_gregorian
except ImportError:
    ordinal_to_gregorian = None

pytestmark = pytest.mark.skipif(
    ordinal_to_gregorian is None, reason="ordinal_to_gregorian function not implemented"
)


@pytest.mark.parametrize(
    "year, day_of_year, expected",
    [
        (2024, 1, (2024, 1, 1)),
        (2024, 32, (2024, 2, 1)),
        (2024, 60, (2024, 2, 29)),  # Leap year
        (2023, 60, (2023, 3, 1)),  # Not leap year
        (2024, 366, (2024, 12, 31)),
        (2023, 365, (2023, 12, 31)),
        (2024, 100, (2024, 4, 9)),
    ],
)
def test_ordinal_to_gregorian(year, day_of_year, expected):
    assert ordinal_to_gregorian(year, day_of_year) == expected
