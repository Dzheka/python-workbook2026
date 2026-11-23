import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("0\n", "1"),
        ("5\n", "120"),
        ("10\n", "3628800"),
    ],
)
def test_factorial(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
