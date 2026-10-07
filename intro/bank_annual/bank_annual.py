balance=float(input("Enter the initial deposit: "))
profit=float(input("Enter annual interest rate (%): "))
year=float(input("Enter the number of years: "))
print(f"Balance after {year:.0f} year (s): {balance * (1+profit/100)**year:.2f}")