initial = input().lower()
final = input().lower()

if initial == final:
    print("No transition")

elif initial == "solid" and final == "liquid":
    print("melting")

elif initial == "liquid" and final == "solid":
    print("freezing")

elif initial == "liquid" and final == "gas":
    print("vaporization")

elif initial == "gas" and final == "liquid":
    print("condensation")

elif initial == "solid" and final == "gas":
    print("sublimation")

elif initial == "gas" and final == "solid":
    print("deposition")

elif initial == "gas" and final == "plasma":
    print("ionization")

elif initial == "plasma" and final == "gas":
    print("recombination")

else:
    print("Cannot transition directly")