import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("9\n", "1\n3\n5\n7\n9"),
        ("6\n", "1\n3\n5"),
        ("1\n", "1"),
    ],
)
def test_odd_numbers(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
