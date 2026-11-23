#101.325

#Pressure in pascals: 101325.00
#Pressure in bars: 1.01
#Pressure in atmospheres: 1.00
#Pascals: Pa = kPa × 1000
#Bars: bar = kPa / 100
#Atmospheres: atm = kPa / 101.325

number = float(input("Enter the pressure in kilopascals: "))
pascals = number * 1000
bars = number / 100
atmospheres = number / 101.325
print(f"Pressure in pascals: {pascals:.2f}")
print(f"Pressure in bars: {bars:.2f}")
print(f"Pressure in atmospheres: {atmospheres:.2f}")
