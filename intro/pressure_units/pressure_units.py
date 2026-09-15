"""Formula
Pascals: Pa = kPa × 1000
Bars: bar = kPa / 100
Atmospheres: atm = kPa / 101.325
output form
Pressure in pascals: 101325.00
Pressure in bars: 1.01
Pressure in atmospheres: 1.00"""

kPa = float(input("kPa"))

pascals = kPa * 1000
bars = kPa / 100
atmospheres = kPa / 101.325

print(f"Pressure in pascals: {pascals:.2f}")
print(f"Pressure in bars: {bars:.2f}")
print(f"Pressure in atmospheres: {atmospheres:.2f}")



