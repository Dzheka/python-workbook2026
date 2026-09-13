pressure = float(input("Enter pressure (Pascals): "))
volume = float(input("Enter volume (liters): "))
temperature = float(input("Enter temperature (°C): "))

volume_m3 = volume / 1000
temperature_k = temperature + 273.15
R = 8.314

moles = pressure * volume_m3 / (R * temperature_k)

print(f"Amount of gas: {moles:.2f} moles")