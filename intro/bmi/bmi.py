"""BMI = weight / (height × height)"""

height = float(input("height:"))
weight = float(input("weight:"))

bmi = weight / height**2

print(f"{bmi:.2f}")