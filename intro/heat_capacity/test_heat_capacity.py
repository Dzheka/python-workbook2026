import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        (
            "2\n90\n",
            "Energy required: 0.21 kWh\nCost to heat water: $0.01",
        ),
        (
            "5\n80\n",
            "Energy required: 0.47 kWh\nCost to heat water: $0.02",
        ),
        (
            "10\n75\n",
            "Energy required: 0.87 kWh\nCost to heat water: $0.03",
        ),
    ],
)
def test_heat_capacity(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
