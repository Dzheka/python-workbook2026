import pytest


@pytest.mark.parametrize(
    "input_values, expected_cost",
    [
        ("5\n10\n65\n40\n\n", "69.00"),
        ("2\n8\n35\n\n", "37.00"),
        ("1\n2\n3\n\n", "14.00"),
        ("70\n68\n\n", "36.00"),
        ("25\n30\n35\n\n", "69.00"),
    ],
)
def test_admission_price(solution, input_values, expected_cost):
    result = solution.run(input_text=input_values)

    assert expected_cost in result.stdout
