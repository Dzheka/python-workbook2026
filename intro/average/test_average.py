import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("10\n20\n30\n", "20.00"),
        ("5\n15\n25\n", "15.00"),
        ("8\n12\n16\n", "12.00"),
    ],
)
def test_average(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
