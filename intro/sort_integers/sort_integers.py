a = int(input())
b = int(input())
c = int(input())

ans = a,b,c
print(*sorted(ans), sep=", ")
