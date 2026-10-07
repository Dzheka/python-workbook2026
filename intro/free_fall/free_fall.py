"""Formula
vf = √(vi² + 2ad) where:

vi = 0 (initial velocity, dropped)
a = 9.8 m/s² (acceleration due to gravity)
d = height (distance fallen)"""

from math import sqrt

d = float(input())

vf  = sqrt(2 * 9.8 * d)
print(f'Final velocity: {vf:.2f} m/s')