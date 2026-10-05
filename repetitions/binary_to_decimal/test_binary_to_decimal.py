import pytest


@pytest.mark.parametrize(
    "binary_input, expected_decimal",
    [
        ("1010", "10"),
        ("1111", "15"),
        ("10000", "16"),
        ("1", "1"),
        ("0", "0"),
        ("11111111", "255"),
        ("101010", "42"),
    ],
)
def test_binary_to_decimal(solution, binary_input, expected_decimal):
    result = solution.run(input_text=f"{binary_input}\n")

    assert expected_decimal in result.stdout
