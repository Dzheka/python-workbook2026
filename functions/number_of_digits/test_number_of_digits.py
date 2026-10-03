import pytest

try:
    from number_of_digits import number_of_digits
except ImportError:
    number_of_digits = None

pytestmark = pytest.mark.skipif(
    number_of_digits is None, reason="number_of_digits function not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (-1, 1),
        (0, 1),
        (7, 1),
        (99, 2),
        (-456, 3),
        (123, 3),
        (12345, 5),
        (1000000, 7),
    ],
)
def test_number_of_digits(n, expected):
    assert number_of_digits(n) == expected
