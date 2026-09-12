volume = float(input("Enter volume of water (liters): "))
temperature_change = float(input("Enter temperature change (°C): "))

energy = volume * 4186 * temperature_change / 3600000
cost = energy * 0.04

print(f"Energy required: {energy:.2f} kWh")
print(f"Cost to heat water: ${cost:.2f}")