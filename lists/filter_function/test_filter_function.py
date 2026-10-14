import pytest

try:
    from filter_function import filter_list
except ImportError:
    filter_list = None

pytestmark = pytest.mark.skipif(
    filter_list is None, reason="filter_list function not implemented"
)


def test_filter_list_even():
    def is_even(x):
        return x % 2 == 0

    assert filter_list([11, 4, 7, 22, 9], is_even) == [4, 22]


def test_filter_list_positive():
    def is_positive(x):
        return x > 0

    assert filter_list([-2, -1, 0, 1, 2], is_positive) == [1, 2]


def test_filter_list_lambda():
    assert filter_list([2, 3, 5, 7, 11], lambda x: x > 3) == [5, 7, 11]


def test_filter_list_empty():
    assert filter_list([2, 3, 5], lambda x: x > 10) == []
