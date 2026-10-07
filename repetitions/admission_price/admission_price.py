money = 0
age = input()

while age != "":
    age = int(age)

    if age <= 2:
        money += 0
    elif age <= 12:
        money += 14
    elif age >= 65:
        money += 18
    else:
        money += 23

    age = input()

print(f"${money:.2f}")