import pytest

try:
    from is_perfect import is_perfect
except ImportError:
    is_perfect = None

pytestmark = pytest.mark.skipif(
    is_perfect is None, reason="is_perfect function not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, False),
        (6, True),
        (12, False),
        (28, True),
        (100, False),
        (496, True),
        (8128, True),
    ],
)
def test_is_perfect(n, expected):
    assert is_perfect(n) == expected
