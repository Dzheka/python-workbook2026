i = input()
a = 0
for j in i:
    if j == '-':
        continue
    a += int(j)
print(a)