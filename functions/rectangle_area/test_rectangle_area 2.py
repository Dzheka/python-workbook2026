import pytest

try:
    from rectangle_area import rectangle_area
except ImportError:
    rectangle_area = None

pytestmark = pytest.mark.skipif(
    rectangle_area is None, reason="rectangle_area function not implemented"
)


@pytest.mark.parametrize(
    "length, width, expected",
    [
        (1, 1, 1),
        (5, 3, 15),
        (10, 2, 20),
        (7.5, 4, 30.0),
        (100, 50, 5000),
        (0.5, 0.5, 0.25),
    ],
)
def test_rectangle_area(length, width, expected):
    assert abs(rectangle_area(length, width) - expected) < 1e-9
