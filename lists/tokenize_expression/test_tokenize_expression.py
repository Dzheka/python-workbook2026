import pytest

try:
    from tokenize_expression import tokenize_expression
except ImportError:
    tokenize_expression = None

pytestmark = pytest.mark.skipif(
    tokenize_expression is None, reason="tokenize_expression function not implemented"
)


@pytest.mark.parametrize(
    "expr, expected",
    [
        ("(5)", ["(", "5", ")"]),
        ("100+200", ["100", "+", "200"]),
        ("3+5*2", ["3", "+", "5", "*", "2"]),
        ("15 - 7 + 2", ["15", "-", "7", "+", "2"]),
        ("(10+20)*3", ["(", "10", "+", "20", ")", "*", "3"]),
        ("1+2+3+4", ["1", "+", "2", "+", "3", "+", "4"]),
    ],
)
def test_tokenize_expression(expr, expected):
    assert tokenize_expression(expr) == expected
