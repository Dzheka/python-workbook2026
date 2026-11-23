deposit=float(input("Enter initial deposit: "))
rate=float(input("Enter annual interest rate (%): "))
years=float(input("Enter number of years: "))
print(f"Balance after {years:.0f} year (s): {deposit * (1+rate/100)**years:.2f}") 
