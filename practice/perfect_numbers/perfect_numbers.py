def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
l = 0
m = 0
k = 0
def classify_number(n):
    global l, m, k
    a = sum_of_divisors(n)
    if a == n:
        l += 1
        return "perfect"
    elif a < n:
        m += 1
        return "deficient"
    else:
        k += 1
        return "abundant"

x = int(input())
y = int(input())

for i in range(x, y + 1):
    print(f"{i} is {classify_number(i)}")
print(f"Perfect: {l}, Abundant: {k}, Deficient: {m}")
