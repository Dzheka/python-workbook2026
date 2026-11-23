a = input().lower()
b = input().lower()

if a == b:
    print("No transition")
elif a == "solid" and b == "liquid":
    print("melting")
elif a == "liquid" and b == "solid":
    print("freezing")
elif a == "liquid" and b == "gas":
    print("vaporization")
elif a == "gas" and b == "liquid":
    print("condensation")
elif a == "solid" and b == "gas":
    print("sublimation")
elif a == "gas" and b == "solid":
    print("deposition")
elif a == "gas" and b == "plasma":
    print("ionization")
elif a == "plasma" and b == "gas":
    print("recombination")
else:
    print("Cannot transition directly")