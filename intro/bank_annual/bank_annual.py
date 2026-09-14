initial_deposit=float(input("Enter the initial deposit: ".strip()))
interest_rate=float(input("Enter the annual interest rate (%): ").strip())   
years=int(input("Enter the number of years: ").strip())
rate_coefficient= interest_rate/100
final_balance= initial_deposit*(1+rate_coefficient)**years
if years==1:
    print(f"Balance after {years} years: {final_balance:.2f}")
else:
    print(f"Balance after {years} years: {final_balance:.2f}")
