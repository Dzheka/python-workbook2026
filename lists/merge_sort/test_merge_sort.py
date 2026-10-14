import pytest

try:
    from merge_sort import merge_sort
except ImportError:
    merge_sort = None

pytestmark = pytest.mark.skipif(
    merge_sort is None, reason="merge_sort function not implemented"
)


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([], [2, 3, 5], [2, 3, 5]),
        ([2, 3, 5], [], [2, 3, 5]),
        ([5], [3], [3, 5]),
        ([2, 3], [5, 7], [2, 3, 5, 7]),
        ([2, 5, 11], [3, 7, 13], [2, 3, 5, 7, 11, 13]),
        ([1, 5, 9], [2, 6, 10], [1, 2, 5, 6, 9, 10]),
    ],
)
def test_merge_sort(list1, list2, expected):
    assert merge_sort(list1, list2) == expected
