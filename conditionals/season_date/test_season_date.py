import pytest


@pytest.mark.parametrize(
    "month, day, expected_output",
    [
        ("January", 15, "Winter"),
        ("January", 1, "Winter"),
        ("February", 14, "Winter"),
        ("February", 28, "Winter"),
        ("March", 19, "Winter"),
        ("March", 20, "Spring"),
        ("MARCH", 21, "Spring"),
        ("March", 25, "Spring"),
        ("April", 1, "Spring"),
        ("april", 10, "Spring"),
        ("May", 15, "Spring"),
        ("june", 15, "Spring"),
        ("June", 20, "Spring"),
        ("June", 21, "Summer"),
        ("July", 4, "Summer"),
        ("August", 15, "Summer"),
        ("September", 21, "Summer"),
        ("September", 22, "Fall"),
        ("October", 31, "Fall"),
        ("November", 15, "Fall"),
        ("December", 20, "Fall"),
        ("December", 21, "Winter"),
        ("December", 25, "Winter"),
    ],
)
def test_season_date(solution, month, day, expected_output):
    solution.check_output(
        input_text=f"{month}\n{day}\n", expected_output=expected_output
    )
