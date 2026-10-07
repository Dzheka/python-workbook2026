n = int(input())
m = int(input())

if n > m:
    d = m
else:
    d = n

while not (m % d == 0) or not (n % d == 0):
    d = d - 1
print(d)
