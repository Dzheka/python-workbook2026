import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        (
            "101.325\n",
            "Pressure in pascals: 101325.00\nPressure in bars: 1.01\nPressure in atmospheres: 1.00",
        ),
        (
            "200\n",
            "Pressure in pascals: 200000.00\nPressure in bars: 2.00\nPressure in atmospheres: 1.97",
        ),
        (
            "50\n",
            "Pressure in pascals: 50000.00\nPressure in bars: 0.50\nPressure in atmospheres: 0.49",
        ),
    ],
)
def test_pressure_units(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
