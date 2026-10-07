import math
sides=int(input("Enter number of sides: "))
length=float(input("Enter side length: "))
area=(sides*length**2)/(4*math.tan(math.pi/sides))
print(f"{area:.2f}")