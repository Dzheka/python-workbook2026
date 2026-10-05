P=int(input("Enter pressure (Pascals): "))
V=float(input("Enter volume (liters): "))
C=int(input("Enter temperature (°C): "))
V/=1000
R=8.314
T=C+273.15
n=P*V/(R*T)
print(f"Amount of gas: {n:.2f} moles")