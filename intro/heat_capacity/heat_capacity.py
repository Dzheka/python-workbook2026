import math
ww=int(input("Enter volume of water (liters): "))
tc=int(input("Enter temperature change (°C): "))
c=4.186
E=(ww*1000)*c*tc
kWh=E/3600000
cost=kWh*0.04
kWh=round(kWh,2)
cost=round(cost,2)
print(f"Energy required: {kWh:.2f} kWh")
print(f"Cost to heat water: ${cost:.2f}")