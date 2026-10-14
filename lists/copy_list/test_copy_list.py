import pytest

try:
    from copy_list import are_different_objects, copy_list
except ImportError:
    copy_list = None
    are_different_objects = None


@pytest.mark.skipif(copy_list is None, reason="copy_list function not implemented")
@pytest.mark.parametrize(
    "items",
    [
        [2, 3, 5, 7, 11],
        [],
        [10],
        ["a", "b", "c"],
        [1, "two", 3.0],
    ],
)
def test_copy_list(items):
    copied = copy_list(items)
    assert copied == items
    assert copied is not items


@pytest.mark.skipif(
    are_different_objects is None,
    reason="are_different_objects function not implemented",
)
def test_are_different_objects():
    l1 = [2, 3, 5]
    l2 = [2, 3, 5]
    l3 = l1

    assert are_different_objects(l1, l2) is True
    assert are_different_objects(l1, l3) is False
