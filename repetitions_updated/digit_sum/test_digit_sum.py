import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("0\n", "0"),
        ("99\n", "18"),
        ("1000\n", "1"),
        ("12345\n", "15"),
    ],
)
def test_digit_sum(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
