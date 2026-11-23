m = float(input("Enter volume of water (liters): "))
dt = int(input("Enter temperature change (°C): ")) 
C = 4.186 
q = m * C * dt 
kWh = q / 3600
cost = kWh * 0.04 
print(f"Energy required: {kWh:.2f} kWh")
print(f"Cost to heat water: ${cost:.2f}")
