import pytest

try:
    from distance_earth import distance_earth
except ImportError:
    distance_earth = None

pytestmark = pytest.mark.skipif(
    distance_earth is None, reason="distance_earth function not implemented"
)


@pytest.mark.parametrize(
    "lat1, lon1, lat2, lon2, expected",
    [
        (0, 0, 0, 0, 0.0),
        (40.7128, -74.0060, 34.0522, -118.2437, 3944),  # NYC to LA (approx)
        (51.5074, -0.1278, 48.8566, 2.3522, 344),  # London to Paris (approx)
        (0, 0, 0, 180, 20015),  # Half Earth's circumference (approx)
    ],
)
def test_distance_earth(lat1, lon1, lat2, lon2, expected):
    result = distance_earth(lat1, lon1, lat2, lon2)
    # Allow 10% tolerance due to approximations
    assert abs(result - expected) < expected * 0.1 or (expected == 0 and result < 1)
