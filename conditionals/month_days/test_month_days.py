import pytest


@pytest.mark.parametrize(
    "month, expected_output",
    [
        ("January", "31"),
        ("february", "28 or 29"),
        ("March", "31"),
        ("April", "30"),
        ("May", "31"),
        ("June", "30"),
        ("July", "31"),
        ("August", "31"),
        ("September", "30"),
        ("October", "31"),
        ("November", "30"),
        ("DECEMBER", "31"),
        ("xyz", "Invalid month"),
        ("", "Invalid month"),
        ("jan", "Invalid month"),
    ],
)
def test_month_days(solution, month, expected_output):
    solution.check_output(input_text=f"{month}\n", expected_output=expected_output)
