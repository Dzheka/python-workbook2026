import pytest

try:
    from binary_search import binary_search
except ImportError:
    binary_search = None

pytestmark = pytest.mark.skipif(
    binary_search is None, reason="binary_search function not implemented"
)


@pytest.mark.parametrize(
    "items, target, expected",
    [
        ([5], 5, 0),
        ([5], 10, -1),
        ([2, 3, 5, 7, 11], 2, 0),
        ([2, 3, 5, 7, 11], 5, 2),
        ([2, 3, 5, 7, 11], 11, 4),
        ([2, 3, 5, 7, 11], 4, -1),
        ([10, 20, 30, 40, 50], 30, 2),
        ([1, 3, 5, 7, 9, 11], 7, 3),
    ],
)
def test_binary_search(items, target, expected):
    assert binary_search(items, target) == expected
