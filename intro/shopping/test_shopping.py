import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("12.50\n3\n", "37.50"),
        ("8.99\n2\n", "17.98"),
        ("15.00\n4\n", "60.00"),
    ],
)
def test_shopping(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
