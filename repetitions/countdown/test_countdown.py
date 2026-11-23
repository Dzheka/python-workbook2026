import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("3\n", "3\n2\n1"),
        ("5\n", "5\n4\n3\n2\n1"),
    ],
)
def test_countdown(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
