import pytest

try:
    from next_rounds import next_rounds
except ImportError:
    next_rounds = None

pytestmark = pytest.mark.skipif(
    next_rounds is None, reason="next_rounds function not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (27, [28, 29, 30]),
        (0, [1, 2, 3]),
        (1, [2, 3, 4]),
        (10, [11, 12, 13]),
        (99, [100, 101, 102]),
    ],
)
def test_next_rounds(n, expected):
    assert next_rounds(n) == expected
