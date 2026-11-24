"""Write a program that classifies a given angle based on its measurement in degrees.

Angle Classifications
Type	Range
Acute Angle	0° < angle < 90°
Right Angle	angle = 90°
Obtuse Angle	90° < angle < 180°
Straight Angle	angle = 180°
Reflex Angle	180° < angle < 360°
Full Rotation	angle = 360°
Invalid Angle	angle ≤ 0° or angle > 360°"""

angle = int(input())

if 0 < angle < 90:
    print('Acute Angle')
elif angle == 90:
    print('Right Angle')
elif 90 < angle < 180:
    print('Obtuse Angle')
elif angle == 180:
    print('Straight Angle')
elif 180 < angle < 360:
    print('Reflex Angle')
elif angle == 360:
    print('Full Rotation')
else:
    print('Invalid Angle')