import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (5, 5, 3, "yes"),
        (1, 2, 3, "no"),
        (7, 3, 7, "yes"),
        (4, 4, 4, "yes"),
        (9, 2, 9, "yes"),
        (1, 1, 2, "yes"),
        (10, 20, 30, "no"),
        (0, 0, 1, "yes"),
        (-1, -1, 5, "yes"),
        (-2, 3, -2, "yes"),
    ],
)
def test_two_equal(solution, a, b, c, expected_output):
    solution.check_output(
        input_text=f"{a}\n{b}\n{c}\n", expected_output=expected_output
    )
