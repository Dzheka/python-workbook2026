import math
a = int(input())
b = int(input())
c = int(input())

disc1 = b**2 - 4*a*c
root1 = (-b + math.sqrt(disc1)) / (2*a)
root2 = (-b - math.sqrt(disc1)) / (2*a)
if disc1 < 0:
    print("No real roots")
elif disc1 == 0:
    print("1 root:", root1)  
else:
    print("2 roots:", root2," and ", root1)