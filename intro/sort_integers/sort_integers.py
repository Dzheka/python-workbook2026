a = int(input())
b = int(input())
c = int(input())

numbers = sorted([a, b, c])

print(*numbers, sep=", ")