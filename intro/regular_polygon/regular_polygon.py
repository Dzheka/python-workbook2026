from math import tan, pi


n = int(input("Enter number of sides: "))
s = int(input("Enter side length: "))
area = (n * s** 2) / (4 * tan(pi / n))
print(f"{area:.2f}")