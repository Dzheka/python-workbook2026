import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("25\n", "Temperature in Fahrenheit: 77.00\nTemperature in Kelvin: 298.15"),
        ("0\n", "Temperature in Fahrenheit: 32.00\nTemperature in Kelvin: 273.15"),
        ("100\n", "Temperature in Fahrenheit: 212.00\nTemperature in Kelvin: 373.15"),
    ],
)
def test_celsius_convert(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
