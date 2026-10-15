import pytest


@pytest.mark.parametrize(
    "year, month, day, expected_output",
    [
        (1900, 2, 28, "1900-03-01"),  # Non-leap year (divisible by 100, not 400)
        (2000, 2, 29, "2000-03-01"),  # Leap year (divisible by 400)
        (2001, 1, 1, "2001-01-02"),  # Regular day in January
        (2004, 2, 29, "2004-03-01"),  # Leap year (divisible by 4)
        (2019, 11, 18, "2019-11-19"),  # Regular day
        (2019, 11, 30, "2019-12-01"),  # End of month
        (2019, 12, 31, "2020-01-01"),  # End of year
        (2020, 1, 31, "2020-02-01"),  # End of January
        (2020, 10, 31, "2020-11-01"),  # End of October
        (2020, 11, 30, "2020-12-01"),  # End of November (30 days)
        (2020, 12, 31, "2021-01-01"),  # End of December
        (2020, 2, 28, "2020-02-29"),  # Leap year February
        (2020, 2, 29, "2020-03-01"),  # Last day of leap year February
        (2020, 3, 31, "2020-04-01"),  # End of March
        (2020, 4, 30, "2020-05-01"),  # End of April (30 days)
        (2020, 5, 31, "2020-06-01"),  # End of May
        (2020, 6, 30, "2020-07-01"),  # End of June (30 days)
        (2020, 7, 31, "2020-08-01"),  # End of July
        (2020, 8, 31, "2020-09-01"),  # End of August
        (2020, 9, 30, "2020-10-01"),  # End of September (30 days)
        (2021, 2, 28, "2021-03-01"),  # Non-leap year February
    ],
)
def test_next_day(solution, year, month, day, expected_output):
    solution.check_output(
        input_text=f"{year}\n{month}\n{day}\n", expected_output=expected_output
    )
