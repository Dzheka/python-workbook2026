import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("5.2\n", "84.95"),
        ("3.7\n", "43.01"),
        ("10.0\n", "314.16"),
    ],
)
def test_circle_area(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
