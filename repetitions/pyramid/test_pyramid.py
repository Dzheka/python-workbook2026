import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "*"),
        ("3\n", "*\n ***\n*****"),
        ("5\n", "*\n   ***\n  *****\n *******\n*********"),
    ],
)
def test_pyramid(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
