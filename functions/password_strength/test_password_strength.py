import pytest

try:
    from password_strength import password_strength
except ImportError:
    password_strength = None

pytestmark = pytest.mark.skipif(
    password_strength is None, reason="password_strength function not implemented"
)


@pytest.mark.parametrize(
    "pwd, expected",
    [
        ("abc", "weak"),
        ("weak", "weak"),
        ("hello", "weak"),
        ("abcdefgh", "weak"),
        ("12345678", "weak"),
        ("Hello123", "medium"),
        ("Medium12", "medium"),
        ("Password1", "medium"),
        ("P@ssw0rd!", "medium"),
        ("MyP@ssw0rd!2", "strong"),
        ("Str0ng!Pass1", "strong"),
        ("ABCD1234!@#$", "strong"),
    ],
)
def test_password_strength(pwd, expected):
    assert password_strength(pwd) == expected
