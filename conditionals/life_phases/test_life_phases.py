import pytest


@pytest.mark.parametrize(
    "age, expected_output",
    [
        (0, "Infant"),
        (1, "Infant"),
        (2, "Toddler"),
        (3, "Toddler"),
        (4, "Toddler"),
        (5, "Child"),
        (8, "Child"),
        (10, "Child"),
        (11, "Adolescent"),
        (15, "Adolescent"),
        (17, "Adolescent"),
        (18, "Young Adult"),
        (25, "Young Adult"),
        (39, "Young Adult"),
        (40, "Middle-aged"),
        (50, "Middle-aged"),
        (64, "Middle-aged"),
        (65, "Senior"),
        (70, "Senior"),
        (100, "Senior"),
        (-5, "Invalid age"),
        (-1, "Invalid age"),
    ],
)
def test_life_phases(solution, age, expected_output):
    solution.check_output(input_text=f"{age}\n", expected_output=expected_output)
