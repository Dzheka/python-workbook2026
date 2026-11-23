kpa = float(input())

pascals = kpa * 1000
bars = kpa / 100
atmospheres = kpa / 101.325

print(f"Pressure in pascals: {pascals:.2f}")
print(f"Pressure in bars: {bars:.2f}")
print(f"Pressure in atmospheres: {atmospheres:.2f}")