import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("10\n", "Distance in feet: 32.81"),
        ("5\n", "Distance in feet: 16.40"),
        ("15\n", "Distance in feet: 49.21"),
    ],
)
def test_distance_conversion(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
