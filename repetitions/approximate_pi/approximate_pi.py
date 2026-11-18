pi = 3
f = 1
print(f"{pi:.2f}")
for i in range(2, 30, 2):
    if f:
        pi = pi + 4 / (i * (i + 1) * (i + 2))
        print(pi)
        f = 0
    else:
        pi = pi - 4 / (i * (i + 1) * (i + 2))
        print(pi)
        f = 1