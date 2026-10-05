angle = int(input())

angle = angle % 360

if angle == 0 or angle == 90 or angle == 180 or angle == 270:
    print("On axis")
elif 0 < angle < 90:
    print("Quadrant I")
elif 90 < angle < 180:
    print("Quadrant II")
elif 180 < angle < 270:
    print("Quadrant III")
else:
    print("Quadrant IV")