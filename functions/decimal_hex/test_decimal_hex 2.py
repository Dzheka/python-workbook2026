import pytest

try:
    from decimal_hex import decimal_hex
except ImportError:
    decimal_hex = None

pytestmark = pytest.mark.skipif(
    decimal_hex is None, reason="decimal_hex function not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (1, "1"),
        (10, "A"),
        (15, "F"),
        (16, "10"),
        (26, "1A"),
        (255, "FF"),
        (2748, "ABC"),
        (4095, "FFF"),
    ],
)
def test_decimal_hex(n, expected):
    assert decimal_hex(n) == expected
