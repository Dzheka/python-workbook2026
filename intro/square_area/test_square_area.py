import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("7.5\n", "56.25"),
        ("12.3\n", "151.29"),
        ("5.0\n", "25.00"),
    ],
)
def test_square_area(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
