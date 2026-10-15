import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("20000000\n12\n20\n", "Amount of gas: 98.47 moles"),
        ("101325\n22.4\n0\n", "Amount of gas: 1.00 moles"),
        ("500000\n5\n25\n", "Amount of gas: 1.01 moles"),
    ],
)
def test_ideal_gas(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
