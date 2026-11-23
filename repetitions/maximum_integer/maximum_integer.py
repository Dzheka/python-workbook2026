import random
maximum = random.randint(1, 100)
updates = 0
print(maximum)
for i in range(99):
    number = random.randint(1, 100)
    if number > maximum:
        maximum = number
        updates += 1
        print(number, "<== Update")
    else:
        print(number)
print("The maximum value found was", maximum)
print("The maximum value was updated", updates, "times")