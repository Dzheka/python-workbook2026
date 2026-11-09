import pytest

try:
    from longest_substring_without_repeating import longest_substring_without_repeating
except ImportError:
    longest_substring_without_repeating = None

pytestmark = pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)


def test_abcabcbb():
    assert longest_substring_without_repeating("abcabcbb") == 3


def test_all_same():
    assert longest_substring_without_repeating("bbbbb") == 1


def test_no_repeats():
    assert longest_substring_without_repeating("abcdef") == 6


def test_empty():
    assert longest_substring_without_repeating("") == 0


def test_single_char():
    assert longest_substring_without_repeating("a") == 1


def test_middle_repeat():
    assert longest_substring_without_repeating("pwwkew") == 3


def test_complex():
    assert longest_substring_without_repeating("dvdf") == 3


def test_long():
    assert longest_substring_without_repeating("abcdefghijklmnop") == 16


def test_two_chars():
    assert longest_substring_without_repeating("ab") == 2


def test_pattern():
    assert longest_substring_without_repeating("abba") == 2


def test_space():
    assert longest_substring_without_repeating("a b c a") == 3


def test_numbers():
    assert longest_substring_without_repeating("12345123") == 5
