"""Example 3:

Enter pressure (Pascals): 500000
Enter volume (liters): 5
Enter temperature (°C): 25
Amount of gas: 1.01 moles
Formula
PV = nRT → n = PV / (RT) where:

P = pressure in Pascals
V = volume in cubic meters (convert from liters: 1 liter = 0.001 m³)
n = amount in moles
R = 8.314 J/(mol·K) (ideal gas constant)
T = temperature in Kelvin = °C + 273.15"""

p = int(input())
v = float(input()) / 1000
t = int(input()) + 273.15

n = p * v /(8.314 * t)

print(f"Amount of gas: {n:.2f} moles")