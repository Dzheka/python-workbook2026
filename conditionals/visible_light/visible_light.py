light = int(input())

if 380 <= light < 450:
    print("Violet")
elif 450 <= light < 495:
    print("Blue")
elif 495 <= light < 570:
    print("Green")
elif 570 <= light < 590:
    print("Yellow")
elif 590 <= light < 620:
    print("Orange")
elif 620 <= light <= 750:
    print("Red")
else:
    print("Outside visible spectrum")