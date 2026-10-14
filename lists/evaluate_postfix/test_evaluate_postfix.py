import pytest

try:
    from evaluate_postfix import evaluate_postfix
except ImportError:
    evaluate_postfix = None

pytestmark = pytest.mark.skipif(
    evaluate_postfix is None, reason="evaluate_postfix function not implemented"
)


@pytest.mark.parametrize(
    "postfix, expected",
    [
        (["5", "3", "+"], 8.0),  # 5 + 3
        (["10", "2", "/"], 5.0),  # 10 / 2
        (["2", "3", "^"], 8.0),  # 2 ^ 3
        (["3", "5", "2", "*", "+"], 13.0),  # 3 + (5 * 2)
        (["3", "5", "+", "2", "*"], 16.0),  # (3 + 5) * 2
        (["15", "7", "1", "1", "+", "-", "/"], 3.0),  # 15 / (7 - (1 + 1))
    ],
)
def test_evaluate_postfix(postfix, expected):
    assert evaluate_postfix(postfix) == pytest.approx(expected)
