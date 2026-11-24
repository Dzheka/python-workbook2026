water_volume = int(input("Enter volume of water (liters): "))
temperature = int(input("Enter temperature change (°C): "))
water_volume = water_volume * 1000
c = 4.186
kwh = 3600000
price = 0.04
energy_joules = water_volume * c * temperature
joules = energy_joules / kwh

print(f"Energy required: {joules:.2f} kWh")
print(f"Cost to heat water: ${joules  * price:.2f}")