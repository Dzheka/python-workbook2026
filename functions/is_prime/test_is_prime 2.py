import pytest

try:
    from is_prime import is_prime
except ImportError:
    is_prime = None

pytestmark = pytest.mark.skipif(
    is_prime is None, reason="is_prime function not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (-5, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (11, True),
        (15, False),
        (17, True),
        (29, True),
        (97, True),
        (100, False),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected
