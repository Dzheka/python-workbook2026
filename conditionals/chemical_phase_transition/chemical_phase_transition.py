start = input().lower()
finish = input().lower()

if start == finish:
    print("No transition")
elif start == "solid" and finish == "liquid":
    print("melting")
elif start == "liquid" and finish == "solid":
    print("freezing")
elif start == "liquid" and finish == "gas":
    print("vaporization")
elif start == "gas" and finish == "liquid":
    print("condensation")
elif start == "solid" and finish == "gas":
    print("sublimation")
elif start == "gas" and finish == "solid":
    print("deposition")
elif start == "gas" and finish == "plasma":
    print("ionization")
elif start == "plasma" and finish == "gas":
    print("recombination")
else:
    print("Cannot transition directly")
