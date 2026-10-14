import pytest

try:
    from sieve_of_eratosthenes import sieve_of_eratosthenes
except ImportError:
    sieve_of_eratosthenes = None

pytestmark = pytest.mark.skipif(
    sieve_of_eratosthenes is None,
    reason="sieve_of_eratosthenes function not implemented",
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, []),
        (2, [2]),
        (10, [2, 3, 5, 7]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
    ],
)
def test_sieve_of_eratosthenes(n, expected):
    assert sieve_of_eratosthenes(n) == expected
