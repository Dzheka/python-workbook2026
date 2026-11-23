note = input().upper()

if note[0] == "C":
    base_frequency = 261.63
elif note[0] == "D":
    base_frequency = 293.66
elif note[0] == "E":
    base_frequency = 329.63
elif note[0] == "F":
    base_frequency = 349.23
elif note[0] == "G":
    base_frequency = 392.00
elif note[0] == "A":
    base_frequency = 440.00
elif note[0] == "B":
    base_frequency = 493.88
else:
    print("Invalid note")
    exit()

octave = int(note[1])

frequency = base_frequency / (2 ** (4 - octave))

print(f"{frequency:.2f}")