import pytest


@pytest.mark.parametrize(
    "temperature, expected_output",
    [
        (-1, "solid"),
        (-10, "solid"),
        (-273, "solid"),
        (-50, "solid"),
        (0, "solid or liquid"),
        (1, "liquid"),
        (25, "liquid"),
        (50, "liquid"),
        (99, "liquid"),
        (100, "liquid or gas"),
        (101, "gas"),
        (150, "gas"),
        (200, "gas"),
    ],
)
def test_h2o_phases(solution, temperature, expected_output):
    solution.check_output(
        input_text=f"{temperature}\n", expected_output=expected_output
    )
