import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("5\n12\n3\n8\n15\n\n", "Minimum: 3\nMaximum: 15"),
        ("-5\n-2\n-10\n-1\n\n", "Minimum: -10\nMaximum: -1"),
        ("7\n\n", "Minimum: 7\nMaximum: 7"),
    ],
)
def test_vanilla_min_max(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
