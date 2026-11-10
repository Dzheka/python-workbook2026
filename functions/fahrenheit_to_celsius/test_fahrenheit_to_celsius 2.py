import pytest

try:
    from fahrenheit_to_celsius import fahrenheit_to_celsius
except ImportError:
    fahrenheit_to_celsius = None

pytestmark = pytest.mark.skipif(
    fahrenheit_to_celsius is None,
    reason="fahrenheit_to_celsius function not implemented",
)


@pytest.mark.parametrize(
    "fahrenheit, expected",
    [
        (-40, -40.0),
        (0, -17.77777777777778),
        (32, 0.0),
        (68, 20.0),
        (98.6, 37.0),
        (212, 100.0),
    ],
)
def test_fahrenheit_to_celsius(fahrenheit, expected):
    assert abs(fahrenheit_to_celsius(fahrenheit) - expected) < 1e-9
