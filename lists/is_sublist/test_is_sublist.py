import pytest

try:
    from is_sublist import is_sublist
except ImportError:
    is_sublist = None

pytestmark = pytest.mark.skipif(
    is_sublist is None, reason="is_sublist function not implemented"
)


@pytest.mark.parametrize(
    "main_list, sub, expected",
    [
        ([2, 3, 5], [], True),
        ([2, 3, 5, 7, 11], [11], True),
        ([2, 3, 5, 7, 11], [2, 3], True),
        ([2, 3, 5, 7, 11], [7, 11], True),
        (["a", "b", "c", "d"], ["b", "c"], True),
        ([2, 3, 5, 7, 11], [3, 7], False),
        ([2, 3, 5, 7, 11], [3, 5, 7], True),
        ([2, 3, 5], [2, 3, 5, 7], False),
    ],
)
def test_is_sublist(main_list, sub, expected):
    assert is_sublist(main_list, sub) == expected
