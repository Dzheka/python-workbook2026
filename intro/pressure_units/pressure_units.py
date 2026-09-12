kilopascals = float(input())

pascals = kilopascals * 1000
bars = kilopascals / 100
atmospheres = kilopascals / 101.325

print(f"Pressure in pascals: {pascals:.2f}")
print(f"Pressure in bars: {bars:.2f}")
print(f"Pressure in atmospheres: {atmospheres:.2f}")