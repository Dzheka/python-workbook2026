i=input().lower()
f=input().lower()
if i==f :
    print("No transition")
elif i=="liquid" and f=="solid":
    print("freezing")
elif i=="solid" and f=="liquid" :
    print("melting")
elif i=="solid" and f=="gas" :
    print("sublimation")
elif i=="gas" and f=="solid" :
    print("deposition")
elif i=="liquid" and f=="gas" :
    print("vaporization")
elif i=="gas" and f=='liquid':
    print("condensation")
elif i=="gas" and f=="plasma":
    print("ionization")
elif i=="plasma" and f=="gas" :
    print("recombination")
else :
    print("Cannot transition directly")
