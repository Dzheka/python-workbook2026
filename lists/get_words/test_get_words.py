import pytest

try:
    from get_words import get_words
except ImportError:
    get_words = None

pytestmark = pytest.mark.skipif(
    get_words is None, reason="get_words function not implemented"
)


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("", []),
        ("One", ["One"]),
        ("Hello world", ["Hello", "world"]),
        ("  multiple   spaces  ", ["multiple", "spaces"]),
        ("Python is fun", ["Python", "is", "fun"]),
        ("a b c d", ["a", "b", "c", "d"]),
    ],
)
def test_get_words(sentence, expected):
    assert get_words(sentence) == expected
