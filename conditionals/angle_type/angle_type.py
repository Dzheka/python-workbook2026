a=int(input())
if a>0 and a<90 :
    print("Acute Angle")
elif a==90:
    print("Right Angle")
elif a>90 and a<180 :
    print("Obtuse Angle")
elif a==180 :
    print("Straight Angle")
elif a>180 and a<360 :
    print("Reflex Angle")
elif a==360:
    print("Full Rotation")
else :
    print("Invalid Angle")