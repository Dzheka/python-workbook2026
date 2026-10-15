angle = int(input())

if 0 < angle < 90:
    print("Acute Angle")
elif angle == 90:
    print("Right Angle")
elif 90 < angle < 180:
    print("Obtuse Angle")
elif angle == 180:
    print("Straight Angle")
elif 180 < angle < 360:
    print("Reflex Angle")
elif angle == 360:
    print("Full Rotation")
elif angle <= 0 or angle > 360:
    print("Invalid Angle")
