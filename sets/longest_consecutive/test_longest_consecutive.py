import pytest

try:
    from longest_consecutive import longest_consecutive
except ImportError:
    longest_consecutive = None

pytestmark = pytest.mark.skipif(
    longest_consecutive is None, reason="longest_consecutive function not implemented"
)


def test_basic_sequence():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longer_sequence():
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_with_duplicates():
    assert longest_consecutive([1, 2, 0, 1]) == 3


def test_empty_list():
    assert longest_consecutive([]) == 0


def test_single_element():
    assert longest_consecutive([5]) == 1


def test_no_consecutive():
    assert longest_consecutive([1, 3, 5, 7]) == 1


def test_all_consecutive():
    assert longest_consecutive([1, 2, 3, 4, 5]) == 5


def test_negative_numbers():
    assert longest_consecutive([-2, -1, 0, 1]) == 4


def test_two_sequences():
    assert longest_consecutive([1, 2, 3, 10, 11, 12, 13]) == 4


def test_all_same():
    assert longest_consecutive([5, 5, 5, 5]) == 1


def test_descending_order():
    assert longest_consecutive([5, 4, 3, 2, 1]) == 5


def test_large_gap():
    assert longest_consecutive([1, 2, 100, 101, 102]) == 3
