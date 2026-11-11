""" Write a program that reads the name of a musical note from the user and displays the note's frequency. The basic version only has to handle the notes of the 4th octave; as an optional challenge, extend it to every note from C0 to C8.

Basic Note Frequencies (4th Octave)
Note	Frequency (Hz)
C4	261.63
D4	293.66
E4	329.63
F4	349.23
G4	392.00
A4	440.00
B4	493.88
Mathematical Relationship (For Extended Version)
The frequency of any note in octave n is half the frequency of the corresponding note in octave n + 1
To calculate: frequency = base_frequency / (2^(4-octave_number))
Where base_frequency is the frequency of the note in the 4th octave"""

note = input().strip().upper()

letter = note[0]
octave = int(note[1])
if note[0] not in "CDEFGAB" or not note[1].isdigit():
    print("Invalid note")
else:
    letter = note[0]
    octave = int(note[1])

    if letter == "C":
        freq = 261.63
    elif letter == "D":
        freq = 293.66
    elif letter == "E":
        freq = 329.63
    elif letter == "F":
        freq = 349.23
    elif letter == "G":
        freq = 392.00
    elif letter == "A":
        freq = 440.00
    elif letter == "B":
        freq = 493.88

    freq = freq / (2 ** (4 - octave))
    print(f"{freq:.2f}")