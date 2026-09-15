#Enter volume of water (liters): 2
#Enter temperature change (°C): 90

#Energy required: 0.21 kWh
#Cost to heat water: $0.01

#Energy: q = m × C × 𝚫T where C = 4.186 J/(g·°C)
#Convert to kWh: 1 kWh = 3,600,000 J
#Cost: cost = kWh × 0.04

volume=float(input("Enter volume of water (liters): "))
temperature_change=float(input("Enter temperature change (°C): "))
mass=volume*1000
energy=mass*4.186*temperature_change
kWh=energy/3600000
cost=kWh*0.04
print(f"Energy required: {kWh:.2f} kWh")
print(f"Cost to heat water: ${cost:.2f}")
