import pytest

try:
    from isomorphic_strings import isomorphic_strings
except ImportError:
    isomorphic_strings = None

pytestmark = pytest.mark.skipif(
    isomorphic_strings is None, reason="isomorphic_strings function not implemented"
)


def test_egg_add():
    assert isomorphic_strings("egg", "add") is True


def test_foo_bar():
    assert isomorphic_strings("foo", "bar") is False


def test_paper_title():
    assert isomorphic_strings("paper", "title") is True


def test_different_lengths():
    assert isomorphic_strings("ab", "abc") is False


def test_same_string():
    assert isomorphic_strings("abc", "abc") is True


def test_empty():
    assert isomorphic_strings("", "") is True


def test_single_char():
    assert isomorphic_strings("a", "b") is True


def test_multiple_mappings():
    assert isomorphic_strings("badc", "baba") is False


def test_reverse_mapping():
    assert isomorphic_strings("ab", "aa") is False


def test_long_matching():
    assert isomorphic_strings("abcdefg", "hijklmn") is True


def test_repeated_pattern():
    assert isomorphic_strings("abab", "xyxy") is True
