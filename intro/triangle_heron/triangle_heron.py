"""s = (s1 + s2 + s3) / 2 (semi-perimeter)
Area = √(s × (s - s1) × (s - s2) × (s - s3))"""

"""Example 1:

3
4
5
6.00"""
from math import sqrt

a = int(input(""))
b = int(input(""))
c = int(input(""))

s = (a + b + c) / 2
Area = sqrt(s * (s - a) * (s - b) * (s - c))

print(f"{Area:.2f}")