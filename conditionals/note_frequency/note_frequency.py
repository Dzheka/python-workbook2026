note = str(input())
note = note.upper()

match note:
    case "C4":
        print(261.63)
    case "D4":
        print(293.66)
    case "E4":
        print(329.63)
    case "F4":
        print(349.23)
    case "G4":
        print(f"{392:.2f}")
    case "A4":
        print(f"{440:.2f}")
    case "B4":
        print(493.88)
    case "C3":
        print(130.81)
    case "A5":
        print(f"{880:.2f}")
    case "C5":
        print(523.26)
    case "A3":
        print(f"{220:.2f}")
    case _:
        print("Invalid note")