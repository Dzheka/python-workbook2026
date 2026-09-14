import pytest


@pytest.mark.parametrize(
    "month_num, expected_output",
    [
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
        (13, "Invalid month number"),
        (0, "Invalid month number"),
        (-1, "Invalid month number"),
        (15, "Invalid month number"),
    ],
)
def test_month_from_int(solution, month_num, expected_output):
    solution.check_output(input_text=f"{month_num}\n", expected_output=expected_output)
