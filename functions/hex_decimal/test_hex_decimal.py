import pytest

try:
    from hex_decimal import hex_decimal
except ImportError:
    hex_decimal = None

pytestmark = pytest.mark.skipif(
    hex_decimal is None, reason="hex_decimal function not implemented"
)


@pytest.mark.parametrize(
    "hex_str, expected",
    [
        ("0", 0),
        ("1", 1),
        ("A", 10),
        ("a", 10),
        ("F", 15),
        ("10", 16),
        ("1A", 26),
        ("FF", 255),
        ("ff", 255),
        ("ABC", 2748),
    ],
)
def test_hex_decimal(hex_str, expected):
    assert hex_decimal(hex_str) == expected
