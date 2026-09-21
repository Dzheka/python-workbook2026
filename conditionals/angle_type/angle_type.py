a = int(input())

if 0<a<90:
    print("Acute Angle")
elif 90<a<180:
    print("Obtuse Angle")
elif 180<a<360:
    print("Reflex Angle")
elif a == 90:
    print("Right Angle")
elif a == 180:
    print("Straight Angle")
elif a == 360:
    print("Full Rotation")
elif a<=0 or a>360:
    print("Invalid Angle")

