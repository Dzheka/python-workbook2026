#Enter bill amount: 45.50
#Enter tip percentage: 18

#Tip amount: 8.19
#  Total amount: 53.69

amount=float(input("Enter bill amount: "))
tip_percentage=float(input("Enter tip percentage: "))
tip_amount=amount*tip_percentage/100
total_amount=amount+tip_amount
print(f"Tip amount: {tip_amount:.2f}")
print(f"Total amount: {total_amount:.2f}")