import pytest

try:
    from two_list_operations import two_list_sum
except ImportError:
    two_list_sum = None

pytestmark = pytest.mark.skipif(
    two_list_sum is None, reason="two_list_sum function not implemented"
)


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([10, 20], [5, 10], [15, 30]),
        ([-5, 10], [5, -10], [0, 0]),
        ([0, 0, 0], [2, 3, 5], [2, 3, 5]),
        ([2, 3, 5], [7, 11, 13], [9, 14, 18]),
    ],
)
def test_two_list_sum(list1, list2, expected):
    assert two_list_sum(list1, list2) == expected
