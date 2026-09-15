import pytest


@pytest.mark.parametrize(
    "year, expected_output",
    [
        (1600, "Leap year"),  # Divisible by 400
        (1700, "Not leap year"),  # Divisible by 100 but not 400
        (1800, "Not leap year"),  # Divisible by 100 but not 400
        (1900, "Not leap year"),  # Divisible by 100 but not 400
        (1996, "Leap year"),  # Divisible by 4 but not 100
        (1997, "Not leap year"),  # Not divisible by 4
        (1998, "Not leap year"),  # Not divisible by 4
        (1999, "Not leap year"),  # Not divisible by 4
        (2000, "Leap year"),  # Divisible by 400
        (2001, "Not leap year"),  # Not divisible by 4
        (2004, "Leap year"),  # Divisible by 4 but not 100
        (2012, "Leap year"),  # Divisible by 4 but not 100
        (2021, "Not leap year"),  # Not divisible by 4
        (2024, "Leap year"),  # Divisible by 4 but not 100
        (2100, "Not leap year"),  # Divisible by 100 but not 400
        (2400, "Leap year"),  # Divisible by 400
    ],
)
def test_leap_year(solution, year, expected_output):
    solution.check_output(input_text=f"{year}\n", expected_output=expected_output)
