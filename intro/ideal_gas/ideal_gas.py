P = int(input("Enter pressure (Pascals): "))
V = float(input("Enter volume (liters): "))
t = int(input("Enter temperature (°C): "))
v = V* 0.001
R = 8.314 
T = t + 273.15
n = P*v / (R*T)
print(f"Amount of gas: {n:.2f} moles")
