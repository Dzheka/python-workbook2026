import pytest


@pytest.mark.parametrize(
    "note, expected_output",
    [
        ("C4", "261.63"),
        ("D4", "293.66"),
        ("E4", "329.63"),
        ("F4", "349.23"),
        ("G4", "392.00"),
        ("A4", "440.00"),
        ("B4", "493.88"),
        ("X4", "Invalid note"),
        ("Z4", "Invalid note"),
        ("c4", "261.63"),  # Test case insensitivity if implemented
        ("a4", "440.00"),  # Test case insensitivity if implemented
        # Extended version tests (if implemented)
        ("C3", "130.81"),
        ("A5", "880.00"),
        ("C5", "523.26"),
        ("A3", "220.00"),
    ],
)
def test_note_frequency(solution, note, expected_output):
    solution.check_output(input_text=f"{note}\n", expected_output=expected_output)
