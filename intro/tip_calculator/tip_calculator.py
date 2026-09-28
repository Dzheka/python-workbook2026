ba=float(input("Enter bill amount:")) 
tp=int(input("Enter tip percentage:"))
tip_amount=ba*(tp/100)
total_amount=ba + tip_amount
print(f"Tip amount: {tip_amount:.2f}")
print(f"Total amount: {total_amount:.2f}")
 