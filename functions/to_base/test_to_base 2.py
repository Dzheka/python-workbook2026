import pytest

try:
    from to_base import to_base
except ImportError:
    to_base = None

pytestmark = pytest.mark.skipif(
    to_base is None, reason="to_base function not implemented"
)


@pytest.mark.parametrize(
    "n, base, expected",
    [
        (0, 10, "0"),
        (10, 2, "1010"),
        (255, 16, "FF"),
        (8, 8, "10"),
        (100, 5, "400"),
        (26, 26, "10"),
        (35, 36, "Z"),
        (1000, 10, "1000"),
        (7, 2, "111"),
    ],
)
def test_to_base(n, base, expected):
    assert to_base(n, base) == expected
