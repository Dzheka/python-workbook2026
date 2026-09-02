import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("3\n", "113.10"),
        ("5\n", "523.60"),
        ("2\n", "33.51"),
    ],
)
def test_sphere_volume(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
