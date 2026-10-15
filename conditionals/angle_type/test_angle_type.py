import pytest


@pytest.mark.parametrize(
    "angle, expected_output",
    [
        (-30, "Invalid Angle"),
        (-1, "Invalid Angle"),
        (0, "Invalid Angle"),
        (1, "Acute Angle"),
        (30, "Acute Angle"),
        (45, "Acute Angle"),
        (60, "Acute Angle"),
        (89, "Acute Angle"),
        (90, "Right Angle"),
        (91, "Obtuse Angle"),
        (120, "Obtuse Angle"),
        (150, "Obtuse Angle"),
        (179, "Obtuse Angle"),
        (180, "Straight Angle"),
        (181, "Reflex Angle"),
        (200, "Reflex Angle"),
        (270, "Reflex Angle"),
        (300, "Reflex Angle"),
        (359, "Reflex Angle"),
        (360, "Full Rotation"),
        (361, "Invalid Angle"),
        (450, "Invalid Angle"),
        (720, "Invalid Angle"),
    ],
)
def test_angle_type(solution, angle, expected_output):
    solution.check_output(input_text=f"{angle}\n", expected_output=expected_output)
