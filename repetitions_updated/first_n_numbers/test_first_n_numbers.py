import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("3\n", "1\n2\n3"),
        ("5\n", "1\n2\n3\n4\n5"),
    ],
)
def test_first_n_numbers(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
