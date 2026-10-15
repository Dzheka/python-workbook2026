import pytest


@pytest.mark.parametrize(
    "input_string, is_palindrome",
    [
        ("go dog", True),
        ("flee to me remote elf", True),
        ("some men interpret nine memos", True),
        ("hello world", False),
        ("race car", True),
        ("not a palindrome", False),
    ],
)
def test_multiword_palindrome(solution, input_string, is_palindrome):
    result = solution.run(input_text=f"{input_string}\n")

    if is_palindrome:
        assert (
            "is a palindrome" in result.stdout.lower()
            or "palindrome" in result.stdout.lower()
        )
    else:
        assert "not" in result.stdout.lower() or "isn't" in result.stdout.lower()
