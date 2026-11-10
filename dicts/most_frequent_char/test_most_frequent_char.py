import pytest

try:
    from most_frequent_char import most_frequent_char
except ImportError:
    most_frequent_char = None

pytestmark = pytest.mark.skipif(
    most_frequent_char is None, reason="most_frequent_char function not implemented"
)


def test_basic():
    assert most_frequent_char("hello") == "l"


def test_tie_returns_any():
    result = most_frequent_char("aabb")
    assert result in ["a", "b"]


def test_single_char():
    assert most_frequent_char("a") == "a"


def test_all_unique():
    result = most_frequent_char("abc")
    assert result in ["a", "b", "c"]


def test_case_sensitive():
    result = most_frequent_char("AaA")
    assert result == "A"


def test_with_spaces():
    result = most_frequent_char("a b c a")
    assert result in ["a", " "]


def test_clear_winner():
    assert most_frequent_char("aaabbc") == "a"


def test_empty_raises_error():
    with pytest.raises(ValueError):
        most_frequent_char("")


def test_numbers_and_letters():
    result = most_frequent_char("111a")
    assert result == "1"


def test_long_text():
    result = most_frequent_char("hello world")
    assert result == "l"
