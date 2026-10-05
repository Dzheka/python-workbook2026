import pytest

try:
    from binary_to_decimal import binary_to_decimal
except ImportError:
    binary_to_decimal = None

pytestmark = pytest.mark.skipif(
    binary_to_decimal is None, reason="binary_to_decimal function not implemented"
)


@pytest.mark.parametrize(
    "binary, expected",
    [
        ("0", 0),
        ("1", 1),
        ("10", 2),
        ("11", 3),
        ("1010", 10),
        ("1111", 15),
        ("10000", 16),
        ("11111111", 255),
    ],
)
def test_binary_to_decimal(binary, expected):
    assert binary_to_decimal(binary) == expected
