a = float(input("Enter initial deposit: "))
b = float(input("Enter annual interest rate (%): "))
c = int(input("Enter number of years: "))
balance = a * (1 + b/1200)**(12*c)

print(f"Balance after {c} years: {balance:.2f}")
