"""Example 1:

Enter bill amount: 45.50
Enter tip percentage: 18
Tip amount: 8.19
Total amount: 53.69"""

bill  = float(input())
tip_percetage = int(input())
tip_amount = bill/100 * tip_percetage
total = tip_amount + bill

print(f"Tip amount: {tip_amount:.2f}")
print(f"Total amount: {total:.2f}")