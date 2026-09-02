import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("1.75\n70.0\n", "22.86"),
        ("1.80\n85.0\n", "26.23"),
        ("1.65\n55.0\n", "20.20"),
    ],
)
def test_bmi(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
