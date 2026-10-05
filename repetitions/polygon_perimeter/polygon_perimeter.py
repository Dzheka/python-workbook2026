import math

a = float(input("Enter the first x-coordinate: "))
b = float(input("Enter the first y-coordinate: "))
c = a
d = b
per = 0
x = input("Enter the next x-coordinate (blank to quit): ")
while x != "":
    x = float(x)
    y = float(input("Enter the next y-coordinate: "))
    distance = math.sqrt((x - c)**2 + (y - d)**2)
    per = per + distance
    c = x
    d = y
    x = input("Enter the next x-coordinate (blank to quit): ")
distance = math.sqrt((a - c)**2 + (b - d)**2)
per = per + distance
print(f"The perimeter of that polygon is {per}")