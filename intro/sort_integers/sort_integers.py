
a = int(input())
b = int(input())
c = int(input())

largest = max(a, b, c)
smallest = min(a, b, c)
middle = (a + b + c) - smallest - largest

print(f"{smallest}, {middle}, {largest}")