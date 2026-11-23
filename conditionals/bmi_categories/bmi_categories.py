w = int(input())
h = float(input())
bb = w / h**2
if bb < 18.5:
    print("Underweight")
elif 18.5 <= bb < 25.0:
    print("Normal weight")
elif 25.0 <= bb < 30.0:
    print("Overweight")
else:
    print("Obese")