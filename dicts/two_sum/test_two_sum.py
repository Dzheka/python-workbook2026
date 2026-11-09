import pytest

try:
    from two_sum import two_sum
except ImportError:
    two_sum = None

pytestmark = pytest.mark.skipif(
    two_sum is None, reason="two_sum function not implemented"
)


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_middle():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_same_value():
    assert two_sum([3, 3], 6) == [0, 1]


def test_not_found():
    assert two_sum([2, 3, 5], 10) is None


def test_negative_numbers():
    result = two_sum([-1, -2, -3, -4], -5)
    assert result in [[0, 3], [1, 2]]


def test_with_zero():
    assert two_sum([0, 1, 0], 0) == [0, 2]


def test_large_numbers():
    assert two_sum([1000000, 2, 3], 1000002) == [0, 1]


def test_first_and_last():
    assert two_sum([2, 3, 5, 7, 11], 13) == [0, 4]


def test_consecutive():
    assert two_sum([2, 3, 5, 7], 5) == [0, 1]


def test_single_element():
    assert two_sum([5], 10) is None


def test_two_elements_match():
    assert two_sum([2, 3], 5) == [0, 1]


def test_two_elements_no_match():
    assert two_sum([2, 3], 7) is None
