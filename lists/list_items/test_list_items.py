import pytest

try:
    from list_items import first_item, last_item, mid_item
except ImportError:
    first_item = None
    mid_item = None
    last_item = None


@pytest.mark.skipif(first_item is None, reason="first_item function not implemented")
@pytest.mark.parametrize(
    "items, expected",
    [
        ([10], 10),
        ([100, 200], 100),
        (["a", "b", "c"], "a"),
        ([2, 3, 5, 7, 11], 2),
    ],
)
def test_first_item(items, expected):
    assert first_item(items) == expected


@pytest.mark.skipif(mid_item is None, reason="mid_item function not implemented")
@pytest.mark.parametrize(
    "items, expected",
    [
        ([10], 10),
        (["a", "b", "c"], "b"),
        ([100, 200, 300], 200),
        ([2, 3, 5, 7], 5),
        ([2, 3, 5, 7, 11], 5),
    ],
)
def test_mid_item(items, expected):
    assert mid_item(items) == expected


@pytest.mark.skipif(last_item is None, reason="last_item function not implemented")
@pytest.mark.parametrize(
    "items, expected",
    [
        ([10], 10),
        ([100, 200], 200),
        (["a", "b", "c"], "c"),
        ([2, 3, 5, 7, 11], 11),
    ],
)
def test_last_item(items, expected):
    assert last_item(items) == expected
