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

notes= {
'C4':	261.63,
'D4':	293.66,
'E4':	329.63,
'F4':	349.23,
'G4':	392.00,
'A4':	440.00,
'B4':	493.88
}

note = input().strip().upper()

if note in notes:
    print(f"The frequency of {note} is {notes[note]} Hz.")
else:
    print("Invalid note entered.")