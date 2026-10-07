def sum_of_divisors(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors

def classify(n):
    if sum_of_divisors(n) == n:
        return "perfect"
    elif sum_of_divisors(n) > n:
        return "abundant"
    elif sum_of_divisors(n) < n:
        return "deficient"

a = int(input())
b = int(input())

n_p = 0
n_a = 0
n_d = 0

if 1 <= a <= b:
    for i in range(a, b + 1):
        print(i ,end="    is  ")
        m = classify(i)
        print(m)
        if m == "perfect":
            n_p += 1
        elif m == "abundant":
            n_a += 1
        elif m == "deficient":
            n_d += 1

print(f"Perfect: {n_p}, Abundant: {n_a}, Deficient: {n_d}")