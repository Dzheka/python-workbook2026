import pytest

try:
    from get_page import get_page
except ImportError:
    get_page = None

pytestmark = pytest.mark.skipif(
    get_page is None, reason="get_page function not implemented"
)


@pytest.mark.parametrize(
    "items, page_num, page_size, expected",
    [
        (["a", "b", "c", "d", "e"], 1, 2, ["a", "b"]),
        (["a", "b", "c", "d", "e"], 2, 2, ["c", "d"]),
        (["a", "b", "c", "d", "e"], 3, 2, ["e"]),
        (["a", "b", "c", "d", "e"], 4, 2, []),
        ([2, 3, 5], 1, 10, [2, 3, 5]),
        ([10, 20, 30, 40, 50, 60], 2, 3, [40, 50, 60]),
    ],
)
def test_get_page(items, page_num, page_size, expected):
    assert get_page(items, page_num, page_size) == expected
