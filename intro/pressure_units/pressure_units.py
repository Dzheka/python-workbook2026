kpa = float(input())

pa = kpa * 1000
bar = kpa / 100
atm = kpa / 101.325

print(f"Pressure in pascals: {pa:.2f}")
print(f"Pressure in bars: {bar:.2f}")
print(f"Pressure in atmospheres: {atm:.2f}")
