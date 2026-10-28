import math
a = float(input())
b = float(input())
c = float(input())
disc1 = b**2 - 4*a*c
if disc1 < 0:
    print("No real roots")
elif disc1 == 0:
    root1 = -b / (2*a) + 0.0
    print(f"1 root: {root1:.2f}")
else:
    root1 = (-b - math.sqrt(disc1)) / (2*a) + 0.0
    root2 = (-b + math.sqrt(disc1)) / (2*a) + 0.0
    print(f"2 roots: {root1:.2f} and {root2:.2f}")