phase1 = str(input())
phase2 = str(input())

phase1 = phase1.lower()
phase2 = phase2.lower()

if phase1 == phase2:
    print("No transition")
elif phase1 == "solid" and phase2 == "liquid":
    print("melting")
elif phase1 == "liquid" and phase2 == "solid":
    print("freezing")
elif phase1 == "liquid" and phase2 == "gas":
    print("vaporization")
elif phase1 == "gas" and phase2 == "liquid":
    print("condensation")
elif phase1 == "solid" and phase2 == "gas":
    print("sublimation")
elif phase1 == "gas" and phase2 == "solid":
    print("deposition")
elif phase1 == "gas" and phase2 == "plasma":
    print("ionization")
elif phase1 == "plasma" and phase2 == "gas":
    print("recombination")
else:
    print("Cannot transition directly")