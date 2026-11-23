total_cost = 0

age_input = input()
while age_input != "":
    age = int(age_input)

    if age <= 2:
        price = 0.00
    elif age <= 12:
        price = 14.00
    elif age >= 65:
        price = 18.00
    else:
        price = 23.00

    total_cost += price
    age_input = input()

print(f"${total_cost:.2f}")
