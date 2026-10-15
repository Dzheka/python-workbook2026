import pytest


@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        ("10\n20\n30\n0\n", "20.0"),
        ("5\n15\n25\n35\n0\n", "20.0"),
        ("100\n0\n", "100.0"),
        ("1\n2\n3\n4\n5\n0\n", "3.0"),
    ],
)
def test_average(solution, input_values, expected_output):
    result = solution.run(input_text=input_values)
    assert expected_output in result.stdout
