import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (1, -5, 6, "2 roots: 2.00 and 3.00"),  # Two roots: 2, 3
        (1, -4, 4, "1 root: 2.00"),  # One root: 2
        (1, 2, 5, "No real roots"),  # No real roots
        (2, -7, 3, "2 roots: 0.50 and 3.00"),  # Two roots: 0.5, 3
        (1, 0, -4, "2 roots: -2.00 and 2.00"),  # Two roots: -2, 2
        (1, -2, 1, "1 root: 1.00"),  # One root: 1
        (1, 0, 1, "No real roots"),  # No real roots
        (1, -6, 9, "1 root: 3.00"),  # One root: 3
        (1, -3, 2, "2 roots: 1.00 and 2.00"),  # Two roots: 1, 2
        (2, -4, 2, "1 root: 1.00"),  # One root: 1
        (1, -1, -6, "2 roots: -2.00 and 3.00"),  # Two roots: -2, 3
        (3, 2, 1, "No real roots"),  # No real roots
        (1, 0, 0, "1 root: 0.00"),  # One root: 0
        (1, -7, 12, "2 roots: 3.00 and 4.00"),  # Two roots: 3, 4
    ],
)
def test_quadratic_roots(solution, a, b, c, expected_output):
    solution.check_output(
        input_text=f"{a}\n{b}\n{c}\n", expected_output=expected_output
    )
