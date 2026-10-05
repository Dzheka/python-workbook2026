kPa=float(input())
Pa=kPa*1000
bar=kPa/100
atm=kPa/101.325
print(f"Pressure in pascals: {Pa:.2f}")
print(f"Pressure in bars: {bar:.2f}")
print(f"Pressure in atmospheres: {atm:.2f}")