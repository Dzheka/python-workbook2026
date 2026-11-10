import pytest

try:
    from decimal_to_binary import decimal_to_binary
except ImportError:
    decimal_to_binary = None

pytestmark = pytest.mark.skipif(
    decimal_to_binary is None, reason="decimal_to_binary function not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (10, "1010"),
        (15, "1111"),
        (16, "10000"),
        (255, "11111111"),
    ],
)
def test_decimal_to_binary(n, expected):
    assert decimal_to_binary(n) == expected
