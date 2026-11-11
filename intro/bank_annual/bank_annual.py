"""Formula
balance = deposit × (1 + rate/100)^years"""

"""Enter initial deposit: 1000.00
Enter annual interest rate (%): 4.5
Enter number of years: 3
Balance after 3 year(s): 1141.17"""

# "1000.00\n4.5\n3\n"

deposit = float(input("Enter initial deposit:"))
annual_interest_rate = float(input("Enter annual interest rate (%):"))
years_num = int(input("Enter number of years:"))

balance = round(deposit * (1 + annual_interest_rate/100)**years_num, 2)

print(f"Balance after {years_num} years: {balance:.2f}")