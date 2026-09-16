import pytest


@pytest.mark.parametrize(
    "number, expected_output",
    [
        (15, "FizzBuzz"),
        (9, "Fizz"),
        (10, "Buzz"),
        (7, "7"),
        (30, "FizzBuzz"),
        (1, "1"),
        (3, "Fizz"),
        (5, "Buzz"),
        (6, "Fizz"),
        (12, "Fizz"),
        (20, "Buzz"),
        (45, "FizzBuzz"),
        (2, "2"),
        (4, "4"),
        (8, "8"),
        (0, "FizzBuzz"),  # 0 is divisible by both 3 and 5
        (-15, "FizzBuzz"),  # Test negative numbers
        (-3, "Fizz"),
        (-5, "Buzz"),
    ],
)
def test_fizz_buzz(solution, number, expected_output):
    solution.check_output(input_text=f"{number}\n", expected_output=expected_output)
