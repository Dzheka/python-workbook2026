"""Write a program that reads a wavelength and reports the corresponding color of visible light.

Visible Light Spectrum
Color	Wavelength Range (nm)
Violet	380 to less than 450
Blue	450 to less than 495
Green	495 to less than 570
Yellow	570 to less than 590
Orange	590 to less than 620
Red	620 to 750"""

nm = int(input())

if 380 <= nm < 450:
    print('Violet')
elif 450 <= nm < 495:
    print('Blue')
elif 495 <= nm < 570:
    print('Green')
elif 570 <= nm < 590:
    print('Yellow')
elif 590 <= nm < 620:
    print('Orange')
elif 620 <= nm <= 750:
    print('Red')
else:
    print('Outside visible spectrum')