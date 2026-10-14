import pytest

try:
    from mark_unary import mark_unary
except ImportError:
    mark_unary = None

pytestmark = pytest.mark.skipif(
    mark_unary is None, reason="mark_unary function not implemented"
)


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["-", "10"], ["~", "10"]),
        (["3", "-", "5"], ["3", "-", "5"]),
        (["-", "5", "+", "3"], ["~", "5", "+", "3"]),
        (["5", "+", "-", "3"], ["5", "+", "~", "3"]),
        (["(", "3", "+", "5", ")"], ["(", "3", "+", "5", ")"]),
        (["(", "-", "5", ")", "*", "2"], ["(", "~", "5", ")", "*", "2"]),
    ],
)
def test_mark_unary(tokens, expected):
    assert mark_unary(tokens) == expected
