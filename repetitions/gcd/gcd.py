a = int(input())
b = int(input())
c = min(a, b)
while (a % c) != 0 or (b % c) != 0:
    c = c - 1
print(c)
