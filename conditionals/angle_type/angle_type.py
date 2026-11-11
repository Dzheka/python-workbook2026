angle = float(input())

if angle <= 0 or angle > 360:
    print("Invalid Angle")
elif angle < 90:
    print("Acute Angle")
elif angle == 90:
    print("Right Angle")
elif angle < 180:
    print("Obtuse Angle")
elif angle == 180:
    print("Straight Angle")
elif angle < 360:
    print("Reflex Angle")
else:
    print("Full Rotation")