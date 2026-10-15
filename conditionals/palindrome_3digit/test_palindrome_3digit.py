import pytest


@pytest.mark.parametrize(
    "number, expected_output",
    [
        (121, "palindrome"),
        (123, "not palindrome"),
        (505, "palindrome"),
        (111, "palindrome"),
        (101, "palindrome"),
        (131, "palindrome"),
        (141, "palindrome"),
        (151, "palindrome"),
        (161, "palindrome"),
        (171, "palindrome"),
        (181, "palindrome"),
        (191, "palindrome"),
        (202, "palindrome"),
        (212, "palindrome"),
        (222, "palindrome"),
        (232, "palindrome"),
        (242, "palindrome"),
        (252, "palindrome"),
        (262, "palindrome"),
        (272, "palindrome"),
        (282, "palindrome"),
        (292, "palindrome"),
        (100, "not palindrome"),
        (200, "not palindrome"),
        (300, "not palindrome"),
        (124, "not palindrome"),
        (789, "not palindrome"),
        (987, "not palindrome"),
        (999, "palindrome"),
    ],
)
def test_palindrome_3digit(solution, number, expected_output):
    solution.check_output(input_text=f"{number}\n", expected_output=expected_output)
