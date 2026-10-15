n = int(input())
s = 1
if n == 0:
    pass
else:
    for i in range(1, n+1):
        s *= i

print(s)

