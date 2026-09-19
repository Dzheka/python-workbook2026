note = input().upper()

letter = note[0]
octave = int(note[1])

if letter == "C":
    frequency = 261.63
elif letter == "D":
    frequency = 293.66
elif letter == "E":
    frequency = 329.63
elif letter == "F":
    frequency = 349.23
elif letter == "G":
    frequency = 392.00
elif letter == "A":
    frequency = 440.00
elif letter == "B":
    frequency = 493.88
else:
    frequency = 0

if frequency == 0 or octave < 0 or octave > 8:
    print("Invalid note")
else:
    frequency = frequency * 2 ** (octave - 4)
    print(f"{frequency:.2f}")