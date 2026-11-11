"""Formula
Volume = (4/3) × π × radius³"""
from math import pi
r = float(input())

volume = 4/3 * pi * r**3

print(f"{volume:.2f}")