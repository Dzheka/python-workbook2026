"""Write a program that reads an angle in degrees and determines which quadrant it falls into on a coordinate plane.

Quadrant Definitions
Quadrant I: 0° < angle < 90°
Quadrant II: 90° < angle < 180°
Quadrant III: 180° < angle < 270°
Quadrant IV: 270° < angle < 360°
Axes: 0°, 90°, 180°, 270°
"""

angle = float(input("Enter angle in degrees: ")) % 360

if angle % 90 == 0:
    print("On axis")
elif 0 < angle < 90:
    print("Quadrant I")
elif 90 < angle < 180:
    print("Quadrant II")
elif 180 < angle < 270:
    print("Quadrant III")
else:
    print("Quadrant IV")