import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("10\n", "Final velocity: 14.00 m/s"),
        ("50\n", "Final velocity: 31.30 m/s"),
        ("100\n", "Final velocity: 44.27 m/s"),
    ],
)
def test_free_fall(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
