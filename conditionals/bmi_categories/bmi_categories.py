"""Write a program that calculates BMI and determines the weight category.
BMI = weight (kg) / height² (m²)
BMI Categories
BMI Range	Category
BMI < 18.5	Underweight
18.5 ≤ BMI < 25.0	Normal weight
25.0 ≤ BMI < 30.0	Overweight
BMI ≥ 30.0	Obese
Examples"""



weight  = float(input())
height = float(input())
bmi = weight / height ** 2
if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi < 25:
    print('Normal weight')
elif 25 <= bmi < 30:
    print('Overweight')
elif bmi >=  30:
    print('Obese')

