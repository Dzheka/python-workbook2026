"""Enter initial deposit: 1000.00
Enter annual interest rate (%): 4.0
Enter number of years: 3
Balance after 3 year(s): 1127.27"""
# balance = principal × (1 + rate/1200)^(12×years)

deposit = float(input("Enter initial deposit:"))
rate = float(input("Enter annual interest rate (%):"))
years = int(input("Enter number of years:"))

balance = deposit * (1 + rate/1200)**(12 * years)

print(f"Balance after {years} years: {balance:.2f}")