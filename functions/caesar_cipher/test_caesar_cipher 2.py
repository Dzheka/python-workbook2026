import pytest

try:
    from caesar_cipher import caesar_cipher
except ImportError:
    caesar_cipher = None

pytestmark = pytest.mark.skipif(
    caesar_cipher is None, reason="caesar_cipher function not implemented"
)


@pytest.mark.parametrize(
    "text, shift, expected",
    [
        ("abc", 1, "bcd"),
        ("xyz", 3, "abc"),
        ("Hello", 5, "Mjqqt"),
        ("ABC", -1, "ZAB"),
        ("Hello, World!", 13, "Uryyb, Jbeyq!"),
        ("xyz", 1, "yza"),
        ("", 5, ""),
    ],
)
def test_caesar_cipher(text, shift, expected):
    assert caesar_cipher(text, shift) == expected
