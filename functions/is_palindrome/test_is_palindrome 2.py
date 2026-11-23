import pytest

try:
    from is_palindrome import is_palindrome
except ImportError:
    is_palindrome = None

pytestmark = pytest.mark.skipif(
    is_palindrome is None, reason="is_palindrome function not implemented"
)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("A", True),
        ("", True),
        ("noon", True),
        ("abc", False),
        ("abba", True),
        ("abcba", True),
        ("abcd", False),
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected
