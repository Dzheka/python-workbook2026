import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("3\n", "1\n12\n123"),
        ("5\n", "1\n12\n123\n1234\n12345"),
    ],
)
def test_number_triangle(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
