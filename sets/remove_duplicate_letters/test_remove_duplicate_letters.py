import pytest

try:
    from remove_duplicate_letters import remove_duplicate_letters
except ImportError:
    remove_duplicate_letters = None

pytestmark = pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)


def test_hello():
    assert remove_duplicate_letters("hello") == "helo"


def test_mississippi():
    assert remove_duplicate_letters("mississippi") == "misp"


def test_abcabc():
    assert remove_duplicate_letters("abcabc") == "abc"


def test_case_sensitive():
    assert remove_duplicate_letters("AaAaBb") == "AaBb"


def test_empty_string():
    assert remove_duplicate_letters("") == ""


def test_no_duplicates():
    assert remove_duplicate_letters("abcdef") == "abcdef"


def test_all_same():
    assert remove_duplicate_letters("aaaa") == "a"


def test_single_char():
    assert remove_duplicate_letters("x") == "x"


def test_with_spaces():
    assert remove_duplicate_letters("a b a b") == "a b"


def test_with_numbers():
    assert remove_duplicate_letters("a1b1c1") == "a1bc"
