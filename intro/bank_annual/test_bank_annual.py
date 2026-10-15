import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("1000.00\n4.5\n3\n", "Balance after 3 years: 1141.17"),
        ("2500.00\n3.25\n5\n", "Balance after 5 years: 2933.53"),
        ("500.00\n2.8\n1\n", "Balance after 1 years: 514.00"),
    ],
)
def test_bank_annual(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
