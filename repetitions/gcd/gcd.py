m = int(input())
n = int(input())

d = min(m, n)

while m % d != 0 or n % d != 0:
    d -= 1

print(d)
