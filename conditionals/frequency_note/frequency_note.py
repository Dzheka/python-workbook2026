"""Reference Note Frequencies (4th Octave)
Note	Frequency (Hz)
C4	261.63
D4	293.66
E4	329.63
F4	349.23
G4	392.00
A4	440.00
B4	493.88
Examples"""

notes = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88
}

try:
    frequency = float(input().strip())
    matched_note = "No match"

    for note, freq in notes.items():
        if abs(frequency - freq) <= 1.0:
            matched_note = note
            break

    print(matched_note)

except (ValueError, EOFError):
    print("No match")