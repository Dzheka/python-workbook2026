import math

import pytest

try:
    from get_hypotenuse import get_hypotenuse
except ImportError:
    get_hypotenuse = None

pytestmark = pytest.mark.skipif(
    get_hypotenuse is None, reason="get_hypotenuse function not implemented"
)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 5.0),
        (5, 12, 13.0),
        (8, 15, 17.0),
        (1, 1, math.sqrt(2)),
        (6, 8, 10.0),
        (9, 12, 15.0),
    ],
)
def test_get_hypotenuse(a, b, expected):
    assert abs(get_hypotenuse(a, b) - expected) < 1e-9
