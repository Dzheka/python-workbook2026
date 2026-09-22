import pytest


@pytest.mark.parametrize(
    "input_value, expected_sequence",
    [
        ("1\n0\n", ["1"]),
        ("3\n0\n", ["3", "10", "5", "16", "8", "4", "2", "1"]),
        ("5\n0\n", ["5", "16", "8", "4", "2", "1"]),
        ("10\n0\n", ["10", "5", "16", "8", "4", "2", "1"]),
    ],
)
def test_collatz(solution, input_value, expected_sequence):
    result = solution.run(input_text=input_value)

    # Check that all numbers in sequence appear in output
    for num in expected_sequence:
        assert num in result.stdout
