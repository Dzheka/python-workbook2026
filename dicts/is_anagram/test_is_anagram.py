import pytest

try:
    from is_anagram import is_anagram
except ImportError:
    is_anagram = None

pytestmark = pytest.mark.skipif(
    is_anagram is None, reason="is_anagram function not implemented"
)


def test_basic_anagrams():
    assert is_anagram("listen", "silent") is True


def test_not_anagrams():
    assert is_anagram("hello", "world") is False


def test_different_lengths():
    assert is_anagram("abc", "abcd") is False


def test_same_word():
    assert is_anagram("test", "test") is True


def test_case_sensitive():
    assert is_anagram("Listen", "silent") is False


def test_empty():
    assert is_anagram("", "") is True


def test_single_char():
    assert is_anagram("a", "a") is True


def test_all_same_chars():
    assert is_anagram("aaa", "aaa") is True


def test_different_order():
    assert is_anagram("abcdef", "fedcba") is True


def test_repeated_chars():
    assert is_anagram("aabbcc", "abcabc") is True


def test_partial_match():
    assert is_anagram("abc", "abd") is False
