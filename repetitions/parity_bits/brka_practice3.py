import math
def sum_of_divisors(n):
    if n == 1:
        return 0
    total = 1
    l = int(math.sqrt(n))
    for i in range(2, l + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total
def classify(n):
    z = sum_of_divisors(n)
    if z == n:
        return "perfect"
    elif z > n:
        return "abundant"
    else:
        return "deficient"

a = int(input())
b = int(input())

for i in range(a, b + 1):
    if classify(i) == "perfect":
        print(i, "is", "perfect", sep=" ")
    elif classify(i) == "abundant":
        print(i, "is", "abundant", sep=" ")
    else:
        print(i, "is", "deficient", sep=" ")
