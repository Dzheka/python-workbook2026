"""Write a program that computes the real roots of a quadratic function using the quadratic formula.

Quadratic Formula
For equation ax² + bx + c = 0:

Discriminant: 𝚫 = b² - 4ac
Roots: x = (-b ± √𝚫) / (2a)
Root Cases
𝚫 < 0: No real roots
𝚫 = 0: One real root
𝚫 > 0: Two real roots
Examples"""
from math import sqrt
a = int(input())
b = int(input())
c = int(input())

delta = b**2 -4*a*c
if delta < 0:
    print('No real roots')
elif delta == 0:
    x = -b/ (2 * a)
    print(f'1 root: {x:.2f}')
elif delta > 0:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print(f'2 roots: {x1:.2f} and {x2:.2f}')