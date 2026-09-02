import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("25\n", "Temperature in Fahrenheit: 77.00"),
        ("0\n", "Temperature in Fahrenheit: 32.00"),
        ("100\n", "Temperature in Fahrenheit: 212.00"),
    ],
)
def test_temperature(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
