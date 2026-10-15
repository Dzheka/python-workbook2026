import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("186330\n", "2:03:45:30"),
        ("88200\n", "1:00:30:00"),
        ("8145\n", "0:02:15:45"),
    ],
)
def test_time_reverse(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
