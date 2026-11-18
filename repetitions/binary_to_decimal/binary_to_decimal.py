n = input()
res = 0
c = 0
for i in n[::-1]:
    res += int(i) * 2 ** c
    c += 1

print(res)