import math 

a = int(input())
b = int(input())
c = int(input())
u = (a + b + c ) / 2
area = math.sqrt(u*(u-a)*(u-b)*(u-c))
print(f"{area:.02f}")