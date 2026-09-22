import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n1\n1\n", "1"),
        ("5\n3\n6\n", "5\n8\n11\n14\n17\n20"),
        ("10\n-2\n5\n", "10\n8\n6\n4\n2"),
    ],
)
def test_arithmetic_sequence(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
