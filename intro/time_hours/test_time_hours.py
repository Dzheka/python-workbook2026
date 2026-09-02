import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("26.5\n", "26.5 hours = 1 days, 2 hours, and 30 minutes"),
        ("50.25\n", "50.25 hours = 2 days, 2 hours, and 15 minutes"),
        ("10.75\n", "10.75 hours = 0 days, 10 hours, and 45 minutes"),
    ],
)
def test_time_hours(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
