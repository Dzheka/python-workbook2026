i = input()
s = 0
for j in i:
    if j == '-':
        continue
    s += int(j)
print(s)
