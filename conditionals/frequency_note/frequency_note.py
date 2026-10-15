frequency = float(input())

if 260.63 <= frequency <= 262.63:
    print("C4")
elif 292.66 <= frequency <= 294.66:
    print("D4")
elif 328.63 <= frequency <= 330.63:
    print("E4")
elif 348.23 <= frequency <= 350.23:
    print("F4")
elif 391 <= frequency <= 393:
    print("G4")
elif 439 <= frequency <= 441:
    print("A4")
elif 492.88 <= frequency <= 494.88:
    print("B4")
else:
    print("No match")