import pytest


@pytest.mark.parametrize(
    "angle1, angle2, angle3, expected_output",
    [
        (60, 60, 60, "Acute Triangle"),
        (90, 45, 45, "Right Triangle"),
        (120, 30, 30, "Obtuse Triangle"),
        (30, 60, 90, "Right Triangle"),
        (45, 45, 90, "Right Triangle"),
        (100, 40, 40, "Obtuse Triangle"),
        (70, 70, 40, "Acute Triangle"),
        (80, 80, 20, "Acute Triangle"),
        (179, 0.5, 0.5, "Obtuse Triangle"),
        (1, 1, 178, "Obtuse Triangle"),
        (30, 30, 120, "Obtuse Triangle"),
        (45, 60, 75, "Acute Triangle"),
    ],
)
def test_triangle_angle_type(solution, angle1, angle2, angle3, expected_output):
    solution.check_output(
        input_text=f"{angle1}\n{angle2}\n{angle3}\n", expected_output=expected_output
    )
