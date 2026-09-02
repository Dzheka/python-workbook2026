import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("5\n", "15"),
        ("10\n", "55"),
        ("100\n", "5050"),
    ],
)
def test_sum_integers(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
