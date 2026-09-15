"""Example 3:

Enter volume of water (liters): 10
Enter temperature change (°C): 75

Energy required: 0.87 kWh
Cost to heat water: $0.03
Formula
Energy: q = m × C × 𝚫T where C = 4.186 J/(g·°C)
Convert to kWh: 1 kWh = 3,600,000 J
Cost: cost = kWh × 0.04"""

volume = float(input())
change = float(input())

energy = 4.186 * change  *  volume / 3600
cost = energy * 0.04

print(f"Energy required: {round(energy, 2):.2f} kWh")
print(f"Cost to heat water: ${round(cost, 2):.2f}")