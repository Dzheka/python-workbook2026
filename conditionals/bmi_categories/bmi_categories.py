weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
elif bmi >= 30:
    print("Obese")