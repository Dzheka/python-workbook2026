wavelength = float(input())

if 380 <= wavelength < 450:
    print("Violet")
elif 450 <= wavelength < 495:
    print("Blue")
elif 495 <= wavelength < 570:
    print("Green")
elif 570 <= wavelength < 590:
    print("Yellow")
elif 590 <= wavelength < 620:
    print("Orange")
elif 620 <= wavelength <= 750:
    print("Red")
else:
    print("Outside visible spectrum")