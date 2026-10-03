import pytest

try:
    from is_even import is_even
except ImportError:
    is_even = None

pytestmark = pytest.mark.skipif(
    is_even is None, reason="is_even function not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (-5, False),
        (-2, True),
        (0, True),
        (1, False),
        (2, True),
        (3, False),
        (4, True),
        (7, False),
        (100, True),
        (101, False),
    ],
)
def test_is_even(n, expected):
    assert is_even(n) == expected
