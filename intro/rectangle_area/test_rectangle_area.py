import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("5.3\n3.2\n", "16.96"),
        ("10.5\n7.8\n", "81.90"),
        ("4.0\n6.5\n", "26.00"),
    ],
)
def test_rectangle_area(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
