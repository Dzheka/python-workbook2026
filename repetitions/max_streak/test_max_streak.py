import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n1\n1\n0\n1\n1\n\n", "Maximum streak: 3"),
        ("1\n1\n1\n1\n1\n\n", "Maximum streak: 5"),
        ("0\n1\n0\n1\n1\n1\n0\n\n", "Maximum streak: 3"),
        ("0\n0\n0\n\n", "Maximum streak: 0"),
    ],
)
def test_max_streak(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
