import pytest


@pytest.mark.parametrize(
    "message, shift, expected_output",
    [
        ("HELLO", "3", "KHOOR"),
        ("xyz", "3", "abc"),
        ("ABC", "1", "BCD"),
        ("XYZ", "3", "ABC"),
        ("Hello World", "5", "Mjqqt Btwqi"),
        ("abc", "-3", "xyz"),
    ],
)
def test_caesar_cipher(solution, message, shift, expected_output):
    result = solution.run(input_text=f"{message}\n{shift}\n")

    assert expected_output in result.stdout
