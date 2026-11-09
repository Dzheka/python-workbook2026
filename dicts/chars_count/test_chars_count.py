import pytest

try:
    from chars_count import chars_count
except ImportError:
    chars_count = None

pytestmark = pytest.mark.skipif(
    chars_count is None, reason="chars_count function not implemented"
)


def test_basic_string():
    assert chars_count("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}


def test_empty_string():
    assert chars_count("") == {}


def test_single_char():
    assert chars_count("a") == {"a": 1}


def test_all_same_char():
    assert chars_count("aaaa") == {"a": 4}


def test_case_sensitive():
    result = chars_count("AaBbCc")
    assert result == {"A": 1, "a": 1, "B": 1, "b": 1, "C": 1, "c": 1}


def test_with_spaces():
    result = chars_count("a b a")
    assert result == {"a": 2, " ": 2, "b": 1}


def test_with_numbers():
    result = chars_count("a1a2")
    assert result == {"a": 2, "1": 1, "2": 1}


def test_string_with_repeating_chars():
    result = chars_count("hello world")
    assert result["l"] == 3
    assert result["o"] == 2
    assert result["h"] == 1


def test_special_characters():
    result = chars_count("a!b@c#")
    assert result == {"a": 1, "!": 1, "b": 1, "@": 1, "c": 1, "#": 1}
