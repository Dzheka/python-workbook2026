import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("6\n4\n", "41.57"),
        ("8\n3\n", "43.46"),
        ("5\n5\n", "43.01"),
    ],
)
def test_regular_polygon(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
