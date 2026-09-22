a = int(input())
b = float(input())
bmi = a/(b*b)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25.0:
    print("Normal weight")
elif 25.0 <= bmi < 30.0 :
    print("Overweight")
elif bmi >= 30.0:
    print("Obese")