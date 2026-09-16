deposit = float(input("Enter initial deposit: "))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

balance = deposit * (1 + rate / 100) ** years

print(f"Balance after {years} year(s): {balance:.2f}")