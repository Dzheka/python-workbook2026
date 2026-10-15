bill = float(input("Enter bill amount: "))
percentage = float(input("Enter tip percentage: "))
tip_amount = (percentage / 100) * bill
print(f"Tip amount: {tip_amount:.2f}")
print(f"Total amount: {bill + tip_amount:.2f}")
