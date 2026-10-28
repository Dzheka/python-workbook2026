volume = float(input("Enter volume of water (liters): "))
temp_change = float(input("Enter temperature change (°C): "))

mass = volume * 1000
energy_j = mass * 4.186 * temp_change
energy_kwh = energy_j / 3600000
cost = energy_kwh * 0.04

print(f"Energy required: {energy_kwh:.2f} kWh")
print(f"Cost to heat water: ${cost:.2f}")