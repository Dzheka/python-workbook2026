import math

n = int(input("Enter number of sides: "))
s = float(input("Enter side length: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(f"{area:.2f}")
