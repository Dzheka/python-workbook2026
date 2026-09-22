a = float(input("Enter bill amount: "))
b = float(input("Enter tip percentage: "))
c = a * b / 100
d = a + a * b / 100
print(f"Tip amount: {c:.02f}")
print(f"Total amount: {d:.02f}")