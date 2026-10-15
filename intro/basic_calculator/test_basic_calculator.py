import pytest


@pytest.mark.parametrize(
    "first_num, second_num, expected_output",
    [
        (12, 8, "12 + 8 = 20\n12 - 8 = 4"),
        (25, 15, "25 + 15 = 40\n25 - 15 = 10"),
        (7, 3, "7 + 3 = 10\n7 - 3 = 4"),
    ],
)
def test_basic_calculator(solution, first_num, second_num, expected_output):
    solution.check_output(
        input_text=f"{first_num}\n{second_num}\n", expected_output=expected_output
    )
