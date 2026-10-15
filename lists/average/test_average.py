import pytest

try:
    from average import average
except ImportError:
    average = None

pytestmark = pytest.mark.skipif(
    average is None, reason="average function not implemented"
)


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([5], 5.0),
        ([-5, 5], 0.0),
        ([100, 200], 150.0),
        ([0, 0, 0], 0.0),
        ([10, 20, 30], 20.0),
        ([2, 3, 5, 7, 11], 5.6),
    ],
)
def test_average(numbers, expected):
    assert average(numbers) == pytest.approx(expected)
