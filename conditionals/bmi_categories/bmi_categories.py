w=int(input())
h=float(input())
bmi=w/(h*h)
if bmi <18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25.0 :
    print("Normal weight")
elif bmi >=25 and bmi<30.0 :
    print("Overweight")
else :
    print("Obese")