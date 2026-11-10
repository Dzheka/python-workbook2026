import random

maximum = random.randint(1, 100)
print(maximum)
update_count = 0

for _ in range(99):
    num = random.randint(1, 100)

    if num > maximum:
        print(f"{num} <== Update")
        maximum = num
        update_count += 1
    else:
        print(num)

print(f"The maximum value found was {maximum}")
print(f"The maximum value was updated {update_count} times")
