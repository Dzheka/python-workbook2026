import random
total = 0
for i in range(10):
    previous = ""
    consecutive = 0
    flips = 0
    while consecutive < 3:
        coin = random.choice("HT")
        print(coin, end=" ")
        flips += 1
        if coin == previous:
            consecutive += 1
        else:
            consecutive = 1
        previous = coin
    print(f"({flips} flips)")
    total += flips
print(f"On average, {total / 10:.1f} flips were needed.")