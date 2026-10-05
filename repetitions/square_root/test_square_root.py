import math

import pytest


@pytest.mark.parametrize(
    "input_value, expected_sqrt",
    [
        ("2", math.sqrt(2)),
        ("16", 4.0),
        ("25", 5.0),
        ("100", 10.0),
        ("144", 12.0),
    ],
)
def test_square_root(solution, input_value, expected_sqrt):
    result = solution.run(input_text=f"{input_value}\n")

    # Extract numeric value from output
    import re

    numbers = re.findall(r"\d+\.\d+", result.stdout)

    if numbers:
        actual = float(numbers[0])
        assert abs(actual - expected_sqrt) < 1e-6
