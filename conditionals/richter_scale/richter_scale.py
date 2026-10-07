"""Write a program that reads an earthquake magnitude and displays the appropriate descriptor according to the Richter scale.

Richter Scale Classifications
Magnitude	Descriptor
magnitude < 2.0	Micro
2.0 <= magnitude < 3.0	Very Minor
3.0 <= magnitude < 4.0	Minor
4.0 <= magnitude < 5.0	Light
5.0 <= magnitude < 6.0	Moderate
6.0 <= magnitude < 7.0	Strong
7.0 <= magnitude < 8.0	Major
8.0 <= magnitude < 10.0	Great
magnitude >= 10.0	Meteoric
Examples"""

magnitude = float(input())

if magnitude < 2.0:
    print("Micro")
elif 2.0 <= magnitude < 3.0:
    print("Very Minor")
elif 3.0 <= magnitude < 4.0:
    print("Minor")
elif 4.0 <= magnitude < 5.0:
    print("Light")
elif 5.0 <= magnitude < 6:
    print("Moderate")
elif 6.0 <= magnitude < 7.0:
    print("Strong")
elif 7.0 <= magnitude < 8.0:
    print("Major")
elif 8.0 <= magnitude < 10.0:
    print('Great')
elif magnitude>= 10:
    print('Meteoric')
