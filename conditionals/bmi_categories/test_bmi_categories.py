import pytest


@pytest.mark.parametrize(
    "weight, height, expected_output",
    [
        (45, 1.65, "Underweight"),  # BMI ≈ 16.53
        (50, 1.70, "Underweight"),  # BMI ≈ 17.30
        (55, 1.70, "Normal weight"),  # BMI ≈ 19.03
        (70, 1.75, "Normal weight"),  # BMI ≈ 22.86
        (60, 1.60, "Normal weight"),  # BMI ≈ 23.44
        (75, 1.75, "Normal weight"),  # BMI ≈ 24.49
        (85, 1.75, "Overweight"),  # BMI ≈ 27.76
        (90, 1.80, "Overweight"),  # BMI ≈ 27.78
        (80, 1.60, "Obese"),  # BMI ≈ 31.25
        (100, 1.75, "Obese"),  # BMI ≈ 32.65
        (120, 1.70, "Obese"),  # BMI ≈ 41.52
    ],
)
def test_bmi_categories(solution, weight, height, expected_output):
    solution.check_output(
        input_text=f"{weight}\n{height}\n", expected_output=expected_output
    )
