import pytest

try:
    from list_to_string import list_to_string
except ImportError:
    list_to_string = None

pytestmark = pytest.mark.skipif(
    list_to_string is None, reason="list_to_string function not implemented"
)


@pytest.mark.parametrize(
    "words, expected",
    [
        ([], ""),
        (["One"], "One"),
        (["Hello", "world"], "Hello world"),
        (["Python", "is", "fun"], "Python is fun"),
        (["a", "b", "c", "d"], "a b c d"),
        (["Test", "multiple", "words", "here"], "Test multiple words here"),
    ],
)
def test_list_to_string(words, expected):
    assert list_to_string(words) == expected
