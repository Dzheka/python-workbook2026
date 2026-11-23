import math

import pytest

try:
    from circle_area import circle_area
except ImportError:
    circle_area = None

pytestmark = pytest.mark.skipif(
    circle_area is None, reason="circle_area function not implemented"
)


@pytest.mark.parametrize(
    "radius, expected",
    [
        (0, 0),
        (1, math.pi),
        (2, math.pi * 4),
        (5, math.pi * 25),
        (10, math.pi * 100),
        (0.5, math.pi * 0.25),
    ],
)
def test_circle_area(radius, expected):
    assert abs(circle_area(radius) - expected) < 1e-9
