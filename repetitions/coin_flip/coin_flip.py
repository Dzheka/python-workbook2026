from random import randint
coins = ['H', 'T']
flips_a = []
for i in range(1, 11):
    c = 0
    flips = 1
    m = coins[randint(0, 1)]
    prev = m
    while c < 3:
        flips += 1
        print(m, end=' ')
        if m == prev:
            c+=1
        else:
            c=1
            prev =m
        m = coins[randint(0, 1)]
    #print(m, end=' ')
    flips_a.append(flips)
    print(f"({flips} flips)")

average = sum(flips_a) / len(flips_a)
print("Average:", average)