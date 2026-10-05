import pytest

try:
    from bmi import bmi
except ImportError:
    bmi = None

pytestmark = pytest.mark.skipif(bmi is None, reason="bmi function not implemented")


@pytest.mark.parametrize(
    "weight, height, expected",
    [
        (70, 1.75, 22.857142857142858),
        (80, 1.80, 24.691358024691358),
        (50, 1.60, 19.53125),
        (90, 1.75, 29.387755102040817),
        (100, 2.0, 25.0),
        (60, 1.70, 20.761245674740486),
    ],
)
def test_bmi(weight, height, expected):
    assert abs(bmi(weight, height) - expected) < 1e-9
