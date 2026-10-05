a=int(input())
if a<0:
    a=a+360


if a>360 :
    a=a-360



if 0<a<90:
    print("Quadrant I")
elif 90<a<180 :
    print("Quadrant II")
elif 180<a<270 :
    print("Quadrant III")
elif 270<a<360 :
    print("Quadrant IV")
else :
    print("On axis")