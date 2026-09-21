import math 

a = int(input("Enter number of sides: "))
b = int(input("enter side length: "))
area = (a*b*b) / (4*math.tan((math.pi)/a))
print(f"{area:.02f}")