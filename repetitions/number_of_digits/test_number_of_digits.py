import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("0\n", "1"),
        ("7\n", "1"),
        ("-987\n", "3"),
        ("12345\n", "5"),
        ("1000000\n", "7"),
    ],
)
def test_number_of_digits(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
