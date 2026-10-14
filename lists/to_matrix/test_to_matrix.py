import pytest

try:
    from to_matrix import to_matrix
except ImportError:
    to_matrix = None

pytestmark = pytest.mark.skipif(
    to_matrix is None, reason="to_matrix function not implemented"
)


@pytest.mark.parametrize(
    "numbers, rows, cols, expected",
    [
        ([2, 3, 5, 7], 2, 2, [[2, 3], [5, 7]]),
        ([2, 3, 5, 7, 11], 1, 5, [[2, 3, 5, 7, 11]]),
        ([2, 3, 5, 7, 11], 5, 1, [[2], [3], [5], [7], [11]]),
        ([2, 3, 5, 7, 11, 13], 2, 3, [[2, 3, 5], [7, 11, 13]]),
        (
            [2, 3, 5, 7, 11, 13, 17, 19, 23],
            3,
            3,
            [[2, 3, 5], [7, 11, 13], [17, 19, 23]],
        ),
    ],
)
def test_to_matrix(numbers, rows, cols, expected):
    assert to_matrix(numbers, rows, cols) == expected
