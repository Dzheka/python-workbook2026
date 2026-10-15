import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("3\n4\n5\n", "6.00"),
        ("5\n6\n7\n", "14.70"),
        ("10\n10\n12\n", "48.00"),
    ],
)
def test_triangle_heron(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
