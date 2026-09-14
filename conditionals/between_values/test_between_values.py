import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (5, 7, 10, "between"),
        (10, 7, 5, "between"),
        (5, 12, 10, "not between"),
        (5, 5, 10, "between"),
        (10, 5, 5, "between"),
        (5, 10, 10, "between"),
        (10, 10, 5, "between"),
        (1, 3, 5, "between"),
        (5, 3, 1, "between"),
        (1, 6, 5, "not between"),
        (5, 6, 1, "not between"),
        (0, 0, 0, "between"),
        (-5, -3, -1, "between"),
        (-1, -3, -5, "between"),
        (-5, 0, -1, "not between"),
        (100, 50, 200, "not between"),
        (200, 50, 100, "not between"),
    ],
)
def test_between_values(solution, a, b, c, expected_output):
    solution.check_output(
        input_text=f"{a}\n{b}\n{c}\n", expected_output=expected_output
    )
