import math

a = float(input())
b = float(input())
c = float(input())

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print("No real roots")
elif discriminant == 0:
    x = 0 if b == 0 else -b / (2 * a)
    print(f"1 root: {x:.2f}")
else:
    x1 = (-b - math.sqrt(discriminant)) / (2 * a)
    x2 = (-b + math.sqrt(discriminant)) / (2 * a)

    print(f"2 roots: {x1:.2f} and {x2:.2f}")