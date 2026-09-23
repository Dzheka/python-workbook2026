import math

a = float(input())
b = float(input())
c = float(input())

discriminant = b**2 - 4 * a * c

if discriminant < 0:
    print("No real roots")
elif discriminant == 0:
    root = -b / (2 * a)
    if root == 0:
        root = 0.0
    print(f"1 root: {root:.2f}")
else:
    root1 = (-b - math.sqrt(discriminant)) / (2 * a)
    root2 = (-b + math.sqrt(discriminant)) / (2 * a)

    if root1 > root2:
        root1, root2 = root2, root1

    print(f"2 roots: {root1:.2f} and {root2:.2f}")