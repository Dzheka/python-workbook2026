import pytest


@pytest.mark.parametrize(
    "sides, expected_output",
    [
        (3, "Triangle"),
        (4, "Quadrilateral"),
        (5, "Pentagon"),
        (6, "Hexagon"),
        (7, "Heptagon"),
        (8, "Octagon"),
        (9, "Nonagon"),
        (10, "Decagon"),
        (2, "Invalid number of sides"),
        (11, "Invalid number of sides"),
        (15, "Invalid number of sides"),
        (0, "Invalid number of sides"),
        (-1, "Invalid number of sides"),
    ],
)
def test_name_shape(solution, sides, expected_output):
    solution.check_output(input_text=f"{sides}\n", expected_output=expected_output)
