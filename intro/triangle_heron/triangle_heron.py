import math

a = float(input())
b = float(input())
c = float(input())

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"{area:.2f}")