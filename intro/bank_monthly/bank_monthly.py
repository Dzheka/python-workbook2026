deposit = float(input())
annual_rate = float(input())
years = int(input())

balance = deposit * (1 + annual_rate / 1200) ** (12 * years)

print(f"Balance after {years} years: {balance:.2f}")