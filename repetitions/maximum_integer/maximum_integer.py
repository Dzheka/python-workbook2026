import random

max = random.randint(1, 100)
print(max)
a = 0
for i in range(99):
    n = random.randint(1, 100)
    if n > max:
        max = n
        a += 1
        print(n, "<== Update")
    else:
        print(n)
print(f"The maximum value found was {max}")
print(f"The maximum value was updated {a} times")