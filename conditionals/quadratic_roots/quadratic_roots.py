a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if d < 0:
    print("No real roots")

elif d == 0:
    x = -b / (2 * a)

    if x == 0:
        x = 0.0

    print(f"1 root: {x:.2f}")

else:
    x1 = (-b - d**0.5) / (2 * a)
    x2 = (-b + d**0.5) / (2 * a)

    print(f"2 roots: {x1:.2f} and {x2:.2f}")