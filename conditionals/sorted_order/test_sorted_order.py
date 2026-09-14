import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (1, 5, 9, "ascending"),
        (9, 5, 1, "descending"),
        (5, 1, 9, "random"),
        (3, 3, 7, "ascending"),
        (8, 4, 4, "descending"),
        (2, 2, 2, "equal"),
        (1, 1, 2, "ascending"),
        (2, 1, 1, "descending"),
        (5, 5, 5, "equal"),
        (10, 5, 15, "random"),
        (15, 10, 5, "descending"),
        (1, 3, 2, "random"),
        (0, 0, 1, "ascending"),
        (1, 0, 0, "descending"),
        (-5, -3, -1, "ascending"),
        (-1, -3, -5, "descending"),
        (-2, 0, 5, "ascending"),
        (5, 0, -2, "descending"),
    ],
)
def test_sorted_order(solution, a, b, c, expected_output):
    solution.check_output(
        input_text=f"{a}\n{b}\n{c}\n", expected_output=expected_output
    )
