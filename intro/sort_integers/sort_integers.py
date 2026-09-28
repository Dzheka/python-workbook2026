a = int(input())
b = int(input())
c = int(input())
all = [a, b, c]
all.sort()
print(*all, sep=", ")
