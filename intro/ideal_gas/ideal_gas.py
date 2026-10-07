p = int(input("Enter pressure (Pascals): "))
v = float(input("Enter volume (liters): "))
t = int(input("Enter temperature (°C): "))

v = v * 0.001 
t = t + 273.15
n = p * v / (8.314 * t)
print(f"Amount of gas: {n:.2f} moles")
