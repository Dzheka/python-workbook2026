import pytest


@pytest.mark.parametrize(
    "letter, expected_output",
    [
        ("a", "vowel"),
        ("b", "consonant"),
        ("y", "sometimes vowel, sometimes consonant"),
        ("A", "vowel"),
        ("e", "vowel"),
        ("i", "vowel"),
        ("o", "vowel"),
        ("u", "vowel"),
        ("E", "vowel"),
        ("I", "vowel"),
        ("O", "vowel"),
        ("U", "vowel"),
        ("Y", "sometimes vowel, sometimes consonant"),
        ("z", "consonant"),
        ("Z", "consonant"),
        ("m", "consonant"),
    ],
)
def test_vowel_consonant(solution, letter, expected_output):
    solution.check_output(input_text=f"{letter}\n", expected_output=expected_output)
