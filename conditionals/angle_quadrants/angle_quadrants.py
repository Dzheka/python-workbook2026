angle = float(input()) % 360

if angle % 90 == 0:
    print("On axis")
elif angle < 90:
    print("Quadrant I")
elif angle < 180:
    print("Quadrant II")
elif angle < 270:
    print("Quadrant III")
else:
    print("Quadrant IV")