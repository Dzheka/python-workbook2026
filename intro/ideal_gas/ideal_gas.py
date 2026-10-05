pressure = float(input("Enter pressure (Pascals): "))
volume = float(input("Enter volume (liters): "))
temperature = float(input("Enter temperature (°C): "))

temperature = temperature + 273.15
volume = volume / 1000

R = 8.314

moles = (pressure * volume) / (R * temperature)

print(f"Amount of gas: {moles:.2f} moles")
