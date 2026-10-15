import pytest


@pytest.mark.parametrize(
    "number, expected_output",
    [
        (7, "odd"),
        (4, "even"),
        (0, "even"),
        (-3, "odd"),
        (-2, "even"),
        (100, "even"),
        (101, "odd"),
    ],
)
def test_even_odd(solution, number, expected_output):
    solution.check_output(input_text=f"{number}\n", expected_output=expected_output)
