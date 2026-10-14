import pytest

try:
    from precedence import precedence
except ImportError:
    precedence = None

pytestmark = pytest.mark.skipif(
    precedence is None, reason="precedence function not implemented"
)


@pytest.mark.parametrize(
    "op, expected",
    [
        ("+", 1),
        ("-", 1),
        ("*", 2),
        ("/", 2),
        ("^", 3),
        ("~", 4),
    ],
)
def test_precedence(op, expected):
    assert precedence(op) == expected


def test_precedence_order():
    assert precedence("+") < precedence("*")
    assert precedence("*") < precedence("^")
    assert precedence("^") < precedence("~")
    assert precedence("+") == precedence("-")
    assert precedence("*") == precedence("/")
