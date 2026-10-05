import random

# Generate first random integer as initial maximum
maximum = random.randint(1, 100)
print(maximum)
update_count = 0

# Generate 99 more random integers
for _ in range(99):
    num = random.randint(1, 100)

    # Check if it's a new maximum
    if num > maximum:
        print(f"{num} <== Update")
        maximum = num
        update_count += 1
    else:
        print(num)

# Display final statistics
print(f"The maximum value found was {maximum}")
print(f"The maximum value was updated {update_count} times")
