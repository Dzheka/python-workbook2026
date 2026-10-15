import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("8\n3\n12\n", "3, 8, 12"),
        ("15\n7\n15\n", "7, 15, 15"),
        ("-5\n10\n0\n", "-5, 0, 10"),
    ],
)
def test_sort_integers(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
