pi = 3
flag = 1
print(f"{pi:.2f}")
for i in range(2, 30, 2):
    if flag:
        pi = pi + 4 / (i * (i + 1) * (i + 2))
        print(pi)
        flag = 0
    else:
        pi = pi - 4 / (i * (i + 1) * (i + 2))
        print(pi)
        flag = 1
