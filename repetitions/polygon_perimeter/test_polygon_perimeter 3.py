import pytest


@pytest.mark.parametrize(
    "input_values, expected_perimeter",
    [
        # Right triangle with sides 1, 1, sqrt(2)
        ("0\n0\n1\n0\n0\n1\n\n", 3.414),
        # Square 2x2
        ("0\n0\n2\n0\n2\n2\n0\n2\n\n", 8.0),
        # Triangle
        ("0\n0\n3\n0\n0\n4\n\n", 12.0),
    ],
)
def test_polygon_perimeter(solution, input_values, expected_perimeter):
    result = solution.run(input_text=input_values)

    # Extract the numeric value from output
    import re

    numbers = re.findall(r"\d+\.\d+", result.stdout)

    if numbers:
        actual = float(numbers[0])
        assert abs(actual - expected_perimeter) < 0.01
