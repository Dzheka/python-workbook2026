bill = float(input("Enter bill amount:"))
tip_percentage = int(input("Enter tip percentage:"))

tip = bill * tip_percentage / 100
total = bill + tip
print(f"Tip amount: {tip:.2f}")
print(f"Total amount: {total:.2f}")
