wavelength = int(input())

if wavelength < 380 or wavelength > 750:
    print("Outside visible spectrum")
elif wavelength < 450:
    print("Violet")
elif wavelength < 495:
    print("Blue")
elif wavelength < 570:
    print("Green")
elif wavelength < 590:
    print("Yellow")
elif wavelength < 620:
    print("Orange")
elif wavelength <= 750:
    print("Red")
