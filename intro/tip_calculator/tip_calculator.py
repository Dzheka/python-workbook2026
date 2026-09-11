bill=float(input("Enter bill amount: "))
percentage=float(input("Enter tip percentage: "))
tip=bill*(percentage/100)
total=bill+tip
print(f"Tip amount: {tip:.2f}")
print(f"Total amount: {total:.2f}")