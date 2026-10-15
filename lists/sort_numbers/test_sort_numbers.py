import pytest

try:
    from sort_numbers import sort_numbers
except ImportError:
    sort_numbers = None

pytestmark = pytest.mark.skipif(
    sort_numbers is None, reason="sort_numbers function not implemented"
)


def test_original_not_modified():
    """Test that the original list is not modified"""
    original = [5, 2, 8, 1, 9]
    original_copy = original.copy()
    sort_numbers(original)
    assert original == original_copy, "Original list should not be modified"


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1], [1]),
        ([5, 2, 3], [2, 3, 5]),
        ([5, 5, 5], [5, 5, 5]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([-5, 0, 5, -10, 10], [-10, -5, 0, 5, 10]),
    ],
)
def test_sort_numbers(numbers, expected):
    assert sort_numbers(numbers) == expected
