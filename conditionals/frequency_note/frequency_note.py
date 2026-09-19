a=float(input())
if abs(a-261.63)<=1:
    print("C4")
elif abs(a-293.66)<=1 :
    print("D4")
elif abs(a-329.63)<=1 :
    print("E4")
elif abs(a-349.23)<=1 :
    print("F4")
elif abs(a-392.00)<=1:
    print("G4")
elif abs(a-440.00)<=1 :
    print("A4")
elif abs(a-493.88)<=1:
    print("B4")
else :
    print("No match")
