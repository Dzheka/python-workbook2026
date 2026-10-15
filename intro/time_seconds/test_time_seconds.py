import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("125\n", "125 second(s) = 2 minute(s) and 5 second(s)"),
        ("90\n", "90 second(s) = 1 minute(s) and 30 second(s)"),
        ("200\n", "200 second(s) = 3 minute(s) and 20 second(s)"),
    ],
)
def test_time_seconds(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
