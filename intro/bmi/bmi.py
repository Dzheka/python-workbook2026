#Enter height in meters: 1.75
#Enter weight in kilograms: 70.0

# 22.86
Height=float(input("Enter height in meters: "))
Weight=float(input("Enter weight in kilograms: "))
BMI=Weight/(Height**2)
print(f"{BMI:.2f}")

