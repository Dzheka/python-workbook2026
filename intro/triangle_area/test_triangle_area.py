import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("10.5\n5.2\n", "27.30"),
        ("8.3\n12.1\n", "50.22"),
        ("15.0\n7.8\n", "58.50"),
    ],
)
def test_triangle_area(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
