import pytest


@pytest.mark.parametrize(
    "year, expected_output",
    [
        (1600, "Saturday"),
        (1700, "Friday"),
        (1800, "Wednesday"),
        (1900, "Monday"),
        (1999, "Friday"),
        (2000, "Saturday"),
        (2001, "Monday"),
        (2017, "Sunday"),
        (2018, "Monday"),
        (2019, "Tuesday"),
        (2020, "Wednesday"),
        (2021, "Friday"),
        (2022, "Saturday"),
        (2023, "Sunday"),
        (2024, "Monday"),
        (2025, "Wednesday"),
        (2100, "Friday"),
        (2200, "Wednesday"),
        (2300, "Monday"),
        (2400, "Saturday"),
    ],
)
def test_january_weekday(solution, year, expected_output):
    solution.check_output(input_text=f"{year}\n", expected_output=expected_output)
