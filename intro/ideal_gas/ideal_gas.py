P = float(input("Enter pressure (Pascals): "))
V = float(input("Enter volume (liters): ")) * 0.001
T = float(input("Enter temperature (°C): ")) + 273.15

n = (P * V) / (8.314 * T)

print(f"Amount of gas: {n:.2f} moles")