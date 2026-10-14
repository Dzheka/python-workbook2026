import pytest

try:
    from to3x3matrix import to3x3matrix
except ImportError:
    to3x3matrix = None

pytestmark = pytest.mark.skipif(
    to3x3matrix is None, reason="to3x3matrix function not implemented"
)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("2 3 5 7 11 13 17 19 23", [[2, 3, 5], [7, 11, 13], [17, 19, 23]]),
        ("23 19 17 13 11 7 5 3 2", [[23, 19, 17], [13, 11, 7], [5, 3, 2]]),
        ("0 0 0 0 0 0 0 0 0", [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ("2 2 2 3 3 3 5 5 5", [[2, 2, 2], [3, 3, 3], [5, 5, 5]]),
    ],
)
def test_to3x3matrix(string, expected):
    assert to3x3matrix(string) == expected
