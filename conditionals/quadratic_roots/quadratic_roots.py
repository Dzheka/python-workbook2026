import math

a = int(input())
b = int(input())
c = int(input())

delta = b** 2 - 4 * a * c 

if delta < 0:
    print("No real roots")
elif delta == 0:
    x = ((-b + math.sqrt(delta)) / (2 * a))
    print(f"1 root: {x:.2f}")
elif delta > 0:
    x = ((-b + math.sqrt(delta)) / (2* a))
    x1 = ((-b - math.sqrt(delta)) / (2 * a))
    print(f"2 roots: {x1:.2f} and {x:.2f}")