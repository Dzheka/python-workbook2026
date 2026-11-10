import pytest

try:
    from password import password
except ImportError:
    password = None

pytestmark = pytest.mark.skipif(
    password is None, reason="password function not implemented"
)


@pytest.mark.parametrize("length", [8, 12, 16, 20])
def test_password_length(length):
    pwd = password(length)
    assert len(pwd) == length


def test_password_contains_all_types():
    pwd = password(20)

    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in "!@#$%^&*()" for c in pwd)

    assert has_lower, "Password should contain lowercase letters"
    assert has_upper, "Password should contain uppercase letters"
    assert has_digit, "Password should contain digits"
    assert has_special, "Password should contain special characters"


def test_password_randomness():
    # Generate multiple passwords and ensure they're different
    passwords = [password(12) for _ in range(10)]
    unique_passwords = set(passwords)

    # At least 9 out of 10 should be unique (very high probability)
    assert len(unique_passwords) >= 9
