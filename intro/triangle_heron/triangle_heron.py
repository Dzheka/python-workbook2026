import math

s1 = float(input())
s2 = float(input())
s3 = float(input())

s = (s1 + s2 + s3) / 2
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print(f"{area:.2f}")