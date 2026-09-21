b = int(input())
a = b%360
if 0<a<90:
    print("Quadrant I")
elif 90<a<180:
    print("Quadrant II")
elif 180<a<270:
    print("Quadrant III")
elif 270<a<360:
    print("Quadrant IV")
elif a ==  0 or a == 90 or a == 180 or a == 270 or a == 360:
    print("On axis")
else :
    print ("Unknown status code")