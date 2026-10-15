import pytest

try:
    from remove_outliers import remove_outliers
except ImportError:
    remove_outliers = None

pytestmark = pytest.mark.skipif(
    remove_outliers is None, reason="remove_outliers function not implemented"
)


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([100, 50, 75], [75]),
        ([10, 5, 8, 3], [5, 8]),
        ([1, 1, 5, 5], [1, 5]),
        ([2, 3, 5, 7, 11], [3, 5, 7]),
        ([3, 1, 4, 1, 5], [3, 4, 1]),
    ],
)
def test_remove_outliers(numbers, expected):
    result = remove_outliers(numbers)
    assert sorted(result) == sorted(expected)
