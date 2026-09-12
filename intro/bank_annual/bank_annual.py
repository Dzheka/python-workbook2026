deposit = float(input())
annual_rate = float(input())
years = int(input())

balance = deposit * (1 + annual_rate / 100) ** years

print(f"Balance after {years} years: {balance:.2f}")