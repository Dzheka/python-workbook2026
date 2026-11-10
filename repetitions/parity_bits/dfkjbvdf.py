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

perfect_count = 0
abundant_count = 0
deficient_count = 0

for i in range(a, b + 1):
    group = classify(i)
    if group == "perfect":
        print(i, "is", "perfect", sep=" ")
        perfect_count += 1
    elif group == "abundant":
        print(i, "is", "abundant", sep=" ")
        abundant_count += 1
    else:
        print(i, "is", "deficient", sep=" ")
        deficient_count += 1

print("perfect:", perfect_count)
print("abundant:", abundant_count)
print("deficient:", deficient_count)