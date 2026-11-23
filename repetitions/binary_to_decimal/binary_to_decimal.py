n = input()
a = 0
c = 0
for i in n[::-1]:
    a += int(i) * 2 ** c
    c += 1
print(a)