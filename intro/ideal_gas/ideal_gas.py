#Enter pressure (Pascals): 20000000
#Enter volume (liters): 12
#Enter temperature (°C): 20

#Amount of gas: 98.47 moles


#PV = nRT → n = PV / (RT) where:

#P = pressure in Pascals
#V = volume in cubic meters (convert from liters: 1 liter = 0.001 m³)
#n = amount in moles
#R = 8.314 J/(mol·K) (ideal gas constant)
#T = temperature in Kelvin = °C + 273.15


pressure=float(input("Enter pressure (Pascals): "))
volume=float(input("Enter volume (liters): "))
temperature=float(input("Enter temperature (°C): "))
volume_m3 = volume * 0.001
temperature_K = temperature + 273.15
n = (pressure * volume_m3) / (8.314 * temperature_K)
print(f"Amount of gas: {n:.2f} moles")
