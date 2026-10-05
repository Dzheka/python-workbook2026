import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("5\n", "15"),
        ("100\n", "5050"),
    ],
)
def test_sum_to_n(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
