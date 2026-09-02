import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("8.5\n5.2\n", "27.40"),
        ("12.3\n4.7\n", "34.00"),
        ("6.0\n6.0\n", "24.00"),
    ],
)
def test_rectangle_perimeter(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
