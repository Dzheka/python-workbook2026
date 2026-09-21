import math

a = int(input())
b = int(input())
c = int(input())
d = min(a,b,c)
e = max(a,b,c)
f = a + b + c - d - e
print(f"{d}, {f}, {e}")