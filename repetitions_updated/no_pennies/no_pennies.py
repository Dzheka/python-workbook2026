# Initialize total
total = 0

# Read prices until blank line
price_input = input()
while price_input != "":
    total += float(price_input)
    price_input = input()

# Calculate cash payment (rounded to nearest nickel)
pennies = round(total * 100)
remainder = pennies % 5

if remainder < 2.5:
    cash_payment = pennies - remainder
else:
    cash_payment = pennies + (5 - remainder)

cash_payment = cash_payment / 100

# Display results
print(f"Total: ${total:.2f}")
print(f"Cash payment: ${cash_payment:.2f}")
