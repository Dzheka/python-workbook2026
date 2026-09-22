c = input()
d = input()
a = c.lower()
b = d.lower()
if a=="liquid" and b=="solid":
    print("freezing")
elif a=="solid" and b=="liquid":
    print("melting")
elif a=="liquid" and b=="gas":
    print("vaporization")
elif a=="gas" and b=="liquid":
    print("condensation")
elif a=="gas" and b=="plasma":
    print("ionization")
elif a=="plasma" and b=="gas":
    print("recombination")
elif a=="solid" and b=="gas":
    print("sublimation")
elif a=="gas" and b=="solid":
    print("deposition")
elif (a=="solid" and b=="plasma") or (a=="plasma" and b=="solid") or (a=="liquid" and b=="plasma") or (a=="plasma" and b=="liquid"):
    print("Cannot transition directly")
else :
    print("No transition")