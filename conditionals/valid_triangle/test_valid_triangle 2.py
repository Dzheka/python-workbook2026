import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (3, 4, 5, "valid triangle"),  # Classic 3-4-5 triangle
        (1, 2, 5, "invalid triangle"),  # 1+2 = 3, not > 5
        (1, 1, 3, "invalid triangle"),  # 1+1 = 2, not > 3
        (5, 5, 8, "valid triangle"),  # 5+5 = 10 > 8
        (10, 10, 20, "invalid triangle"),  # 10+10 = 20, not > 20
        (6, 8, 10, "valid triangle"),  # 6-8-10 triangle
        (1, 1, 1, "valid triangle"),  # Equilateral triangle
        (2, 3, 4, "valid triangle"),  # All conditions met
        (1, 10, 12, "invalid triangle"),  # 1+10 = 11, not > 12
        (7, 10, 16, "valid triangle"),  # 7+10 = 17 > 16
        (5, 12, 13, "valid triangle"),  # 5-12-13 triangle
        (1, 2, 3, "invalid triangle"),  # 1+2 = 3, not > 3
        (0, 1, 1, "invalid triangle"),  # Includes zero (not positive)
        (2, 2, 3, "valid triangle"),  # 2+2 = 4 > 3
        (100, 1, 1, "invalid triangle"),  # 1+1 = 2, not > 100
    ],
)
def test_valid_triangle(solution, a, b, c, expected_output):
    solution.check_output(
        input_text=f"{a}\n{b}\n{c}\n", expected_output=expected_output
    )
