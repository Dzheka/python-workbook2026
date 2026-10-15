import pytest

try:
    from sublists import sublists
except ImportError:
    sublists = None

pytestmark = pytest.mark.skipif(
    sublists is None, reason="sublists function not implemented"
)


@pytest.mark.parametrize(
    "items, expected_count",
    [
        ([2, 3, 5], 7),  # [], [2], [2,3], [2,3,5], [3], [3,5], [5]
        ([2, 3], 4),  # [], [2], [2,3], [3]
        ([2], 2),  # [], [2]
        ([], 1),  # []
    ],
)
def test_sublists_count(items, expected_count):
    result = sublists(items)
    assert len(result) == expected_count


def test_sublists_content():
    result = sublists([2, 3, 5])
    assert [] in result
    assert [2] in result
    assert [3] in result
    assert [5] in result
    assert [2, 3] in result
    assert [3, 5] in result
    assert [2, 3, 5] in result
