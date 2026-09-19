import pytest


@pytest.mark.parametrize(
    "decibel_level, expected_output",
    [
        (0, "Quieter than Quiet Room"),
        (25, "Quieter than Quiet Room"),
        (35, "Quieter than Quiet Room"),
        (40, "Quiet Room"),
        (50, "Between Quiet Room and Alarm Clock"),
        (55, "Between Quiet Room and Alarm Clock"),
        (70, "Alarm Clock"),
        (80, "Between Alarm Clock and Gas Lawnmower"),
        (90, "Between Alarm Clock and Gas Lawnmower"),
        (106, "Gas Lawnmower"),
        (115, "Between Gas Lawnmower and Jackhammer"),
        (120, "Between Gas Lawnmower and Jackhammer"),
        (130, "Jackhammer"),
        (140, "Louder than Jackhammer"),
        (145, "Louder than Jackhammer"),
        (200, "Louder than Jackhammer"),
    ],
)
def test_sound_levels(solution, decibel_level, expected_output):
    solution.check_output(
        input_text=f"{decibel_level}\n", expected_output=expected_output
    )
