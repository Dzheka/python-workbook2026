import pytest

try:
    from pangram_checker import is_pangram
except ImportError:
    is_pangram = None

pytestmark = pytest.mark.skipif(
    is_pangram is None, reason="is_pangram function not implemented"
)


def test_classic_pangram():
    assert is_pangram("The quick brown fox jumps over the lazy dog") is True


def test_another_pangram():
    assert is_pangram("Pack my box with five dozen liquor jugs") is True


def test_not_pangram():
    assert is_pangram("Hello World") is False


def test_lowercase_alphabet():
    assert is_pangram("abcdefghijklmnopqrstuvwxyz") is True


def test_uppercase_alphabet():
    assert is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") is True


def test_empty_string():
    assert is_pangram("") is False


def test_missing_one_letter():
    assert is_pangram("abcdefghijklmnopqrstuvwxy") is False  # missing z


def test_with_numbers_and_punctuation():
    assert is_pangram("The quick brown fox jumps over the lazy dog! 123") is True


def test_repeated_letters():
    assert is_pangram("aaaabcdefghijklmnopqrstuvwxyz") is True


def test_mixed_case_pangram():
    assert is_pangram("ABCDEFGHIJKLMnopqrstuvwxyz") is True


def test_only_numbers():
    assert is_pangram("1234567890") is False
