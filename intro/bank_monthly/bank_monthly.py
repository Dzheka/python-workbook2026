principal = float(input("Enter initial deposit: "))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

balance = principal * (1 + rate / 1200)** (12 * years)
print(f"Balance after {years} years: {balance:.2f}")