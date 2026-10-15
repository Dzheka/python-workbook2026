import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("45.50\n18\n", "Tip amount: 8.19\nTotal amount: 53.69"),
        ("30.00\n20\n", "Tip amount: 6.00\nTotal amount: 36.00"),
        ("85.75\n15\n", "Tip amount: 12.86\nTotal amount: 98.61"),
    ],
)
def test_tip_calculator(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
