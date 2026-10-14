import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Hello123!@#\n", "Very Strong"),
        ("Hello123\n", "Strong"),
        ("hello123\n", "Medium"),
        ("HELLO123\n", "Medium"),
        ("HelloWorld\n", "Medium"),
        ("Hel!23\n", "Strong"),
        ("hello\n", "Very Weak"),
        ("12345\n", "Very Weak"),
    ],
)
def test_password_strength(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
