import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("10\n", "2\n4\n6\n8\n10"),
        ("7\n", "2\n4\n6"),
        ("2\n", "2"),
    ],
)
def test_even_numbers(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
