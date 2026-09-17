from math import tan
n = int(input("Enter number of sides: "))
s = int(input("Enter side length: "))
pi = 3.14159
Area = (n * s**2) / (4 * tan(pi/n)) 
print(f"{Area:.2f}")
