bill=float(input("Enter bill amount: "))
tip=float(input("Enter tip percentage: "))
print(f"Tip amount: {bill*tip/100:.2f}")
print(f"Total amount: {bill*tip/100+bill:.2f}")