"""Formula
Area = (n × s²) / (4 × tan(π/n)) where:

n = number of sides
s = side length"""
from math import tan
from math import pi

n = int(input())
length = float(input())

area = (n * length**2) / (4 * tan(pi/n))

print(f"{area:.2f}")
