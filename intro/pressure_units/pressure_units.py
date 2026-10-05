pressure = float(input())

pascals = pressure * 1000
bars = pressure / 100
atmospheres = pressure / 101.325

print(f"Pressure in pascals: {pascals:.2f}")
print(f"Pressure in bars: {bars:.2f}")
print(f"Pressure in atmospheres: {atmospheres:.2f}")
