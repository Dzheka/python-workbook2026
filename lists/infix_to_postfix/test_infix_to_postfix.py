import pytest

try:
    from infix_to_postfix import infix_to_postfix
except ImportError as missing:
    # This exercise imports `precedence`, so the import can fail for two
    # reasons. Name the one that actually failed instead of always blaming
    # infix_to_postfix.
    unresolved = missing.name
else:
    unresolved = None

pytestmark = pytest.mark.skipif(
    unresolved is not None, reason=f"{unresolved} not implemented"
)


@pytest.mark.parametrize(
    "infix, expected",
    [
        (["3", "+", "5"], ["3", "5", "+"]),
        (["3", "*", "5"], ["3", "5", "*"]),
        (["(", "3", "+", "5", ")"], ["3", "5", "+"]),
        (["3", "+", "5", "+", "2"], ["3", "5", "+", "2", "+"]),
        (["3", "+", "5", "*", "2"], ["3", "5", "2", "*", "+"]),
        (["(", "3", "+", "5", ")", "*", "2"], ["3", "5", "+", "2", "*"]),
    ],
)
def test_infix_to_postfix(infix, expected):
    assert infix_to_postfix(infix) == expected
