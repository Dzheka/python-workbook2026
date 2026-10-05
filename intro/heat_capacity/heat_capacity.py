volume = float(input("Enter volume of water (liters): "))
temperature = float(input("Enter temperature change (°C): "))

mass = volume * 1000
q = mass * 4.186 * temperature

kwh = q / 3600000
cost = kwh * 0.04

print(f"Energy required: {kwh:.2f} kWh")
print(f"Cost to heat water: ${cost:.2f}")
