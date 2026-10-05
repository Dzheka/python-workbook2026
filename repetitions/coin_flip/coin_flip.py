import random

total_flips = 0
for simulation in range(10):
    previous = random.choice(["H", "T"])
    print(previous, end=" ")

    consecutive = 1
    flips = 1
    while consecutive < 3:
        current = random.choice(["H", "T"])
        print(current, end=" ")
        flips += 1
        if current == previous:
            consecutive += 1
        else:
            consecutive = 1
        previous = current
    print(f"({flips} flips)")
    total_flips += flips
average = total_flips / 10
print(f"On average, {average:.1f} flips were needed.")