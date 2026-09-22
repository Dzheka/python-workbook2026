import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("3\n", "1\n 121\n12321"),
        ("5\n", "1\n   121\n  12321\n 1234321\n123454321"),
    ],
)
def test_number_pyramid(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
