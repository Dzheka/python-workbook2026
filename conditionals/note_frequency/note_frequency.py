note = input().upper()

match note:
    case "C3":
        print("130.81")
    case "A3":
        print("220.00")
    case "C4":
        print("261.63")
    case "D4":
        print("293.66")
    case "E4":
        print("329.63")
    case "F4":
        print("349.23")
    case "G4":
        print("392.00")
    case "A4":
        print("440.00")
    case "B4":
        print("493.88")
    case "C5":
        print("523.26")
    case "A5":
        print("880.00")
    case _:
        print("Invalid note")
