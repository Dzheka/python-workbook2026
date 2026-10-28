angle = int(input()) % 360

if angle == 0 or angle == 90 or angle == 180 or angle == 270:
    print("On axis")
elif angle < 90:
    print("Quadrant I")
elif angle < 180:
    print("Quadrant II")
elif angle < 270:
    print("Quadrant III")
else:
    print("Quadrant IV")
