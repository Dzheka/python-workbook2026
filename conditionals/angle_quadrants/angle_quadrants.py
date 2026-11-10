n = int(input())
n = n % 360

if n == 0 or n == 90 or n == 180 or n == 270:
    print("On axis")
elif n < 90:
    print("Quadrant I ")
elif n < 180:
    print("Quadrant II")
elif n < 270:
    print("Quadrant III")
elif n < 360:
    print("Quadrant IV")
