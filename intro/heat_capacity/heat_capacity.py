a = int(input("Enter volume of water (liters): "))
b = int(input("Enter temperature change (°C): "))
c = (a * b) / 3600 * 4.186
d = c * 0.04
print(f"Energy required: {c:.02f} kWh")
print(f"Cost to heat water: ${d:.02f}")