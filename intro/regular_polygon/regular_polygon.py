import math

sides = int(input("Enter number of sides: "))
side_length = float(input("Enter side length: "))

area = (sides * side_length ** 2) / (4 * math.tan(math.pi / sides))

print(f"{area:.2f}")