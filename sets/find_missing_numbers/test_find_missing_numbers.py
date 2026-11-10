import pytest

try:
    from find_missing_numbers import find_missing
except ImportError:
    find_missing = None

pytestmark = pytest.mark.skipif(
    find_missing is None, reason="find_missing function not implemented"
)


def test_missing_in_middle():
    assert find_missing([1, 2, 4, 6], 6) == [3, 5]


def test_multiple_missing():
    assert find_missing([2, 3, 7, 8], 10) == [1, 4, 5, 6, 9, 10]


def test_none_missing():
    assert find_missing([1, 2, 3], 3) == []


def test_empty_list():
    assert find_missing([], 5) == [1, 2, 3, 4, 5]


def test_with_duplicates():
    assert find_missing([1, 1, 2, 2], 4) == [3, 4]


def test_single_element():
    assert find_missing([1], 3) == [2, 3]


def test_all_missing():
    assert find_missing([], 3) == [1, 2, 3]


def test_n_is_one():
    assert find_missing([], 1) == [1]
    assert find_missing([1], 1) == []


def test_numbers_outside_range():
    assert find_missing([1, 2, 10, 20], 5) == [3, 4, 5]


def test_n_is_zero():
    assert find_missing([1, 2, 3], 0) == []
