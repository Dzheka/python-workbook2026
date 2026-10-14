import pytest

try:
    from is_int import is_int
except ImportError:
    is_int = None

pytestmark = pytest.mark.skipif(
    is_int is None, reason="is_int function not implemented"
)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", False),
        ("+", False),
        ("-", False),
        ("-456", True),
        ("-0", True),
        ("0", True),
        ("+0", True),
        ("123", True),
        ("+789", True),
        ("12.5", False),
        ("12a", False),
        ("abc", False),
        ("  123", False),
        ("123  ", False),
    ],
)
def test_is_int(s, expected):
    assert is_int(s) == expected
