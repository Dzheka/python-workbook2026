deposit =float(input("Enter the initial deposit: ".strip()))
rate=float(input("Enter the annual interest rate (%): ").strip())   
years=int(input("Enter the number of years: ").strip())

montly_rate= rate /100 / 12
months= years * 12
balance= deposit * (1 + montly_rate) ** months
print(f"Balance after {years} years: {balance:.2f}")
