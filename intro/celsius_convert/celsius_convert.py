"""Fahrenheit: F = (C × 9/5) + 32
Kelvin: K = C + 273.15"""
"""Temperature in Fahrenheit: 212.00
Temperature in Kelvin: 373.15"""

Celsius = int(input())

Fahrenheit  = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15

print(f"Temperature in Fahrenheit: {Fahrenheit:.2f}")
print(f"Temperature in Kelvin: {Kelvin:.2f}")