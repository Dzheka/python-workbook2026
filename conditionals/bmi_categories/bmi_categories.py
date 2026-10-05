weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal weight")
elif bmi < 30.0:
    print("Overweight")
else:
    print("Obese")