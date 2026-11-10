import pytest

try:
    from digit_sum import digit_sum
except ImportError:
    digit_sum = None

pytestmark = pytest.mark.skipif(
    digit_sum is None, reason="digit_sum function not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1000, 1),
        (123, 6),
        (7, 7),
        (-456, 15),
        (12345, 15),
        (99, 18),
        (-999, 27),
    ],
)
def test_digit_sum(n, expected):
    assert digit_sum(n) == expected
