import pytest


@pytest.mark.parametrize(
    "year, expected_output",
    [
        (-1, "Invalid year"),
        (0, "Invalid year"),
        (1, "Freshman"),
        (2, "Sophomore"),
        (3, "Junior"),
        (4, "Senior"),
        (5, "Invalid year"),
    ],
)
def test_student_year_level(solution, year, expected_output):
    solution.check_output(input_text=f"{year}\n", expected_output=expected_output)
