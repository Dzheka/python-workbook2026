import pytest


@pytest.mark.parametrize(
    "number, expected_output",
    [
        (5, "positive"),
        (-3, "negative"),
        (0, "zero"),
        (100, "positive"),
        (-100, "negative"),
        (1, "positive"),
        (-1, "negative"),
    ],
)
def test_number_sign(solution, number, expected_output):
    solution.check_output(input_text=f"{number}\n", expected_output=expected_output)
