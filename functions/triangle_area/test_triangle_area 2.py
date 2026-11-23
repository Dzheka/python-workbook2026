import pytest

try:
    from triangle_area import triangle_area
except ImportError:
    triangle_area = None

pytestmark = pytest.mark.skipif(
    triangle_area is None, reason="triangle_area function not implemented"
)


@pytest.mark.parametrize(
    "base, height, expected",
    [
        (1, 1, 0.5),
        (10, 5, 25.0),
        (6, 8, 24.0),
        (7.5, 4, 15.0),
        (100, 50, 2500.0),
        (3, 4, 6.0),
    ],
)
def test_triangle_area(base, height, expected):
    assert abs(triangle_area(base, height) - expected) < 1e-9
