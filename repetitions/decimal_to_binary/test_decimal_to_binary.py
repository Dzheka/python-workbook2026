import pytest


@pytest.mark.parametrize(
    "decimal_input, expected_binary",
    [
        ("10", "1010"),
        ("15", "1111"),
        ("42", "101010"),
        ("1", "1"),
        ("0", "0"),
        ("255", "11111111"),
        ("16", "10000"),
    ],
)
def test_decimal_to_binary(solution, decimal_input, expected_binary):
    result = solution.run(input_text=f"{decimal_input}\n")

    assert expected_binary in result.stdout
