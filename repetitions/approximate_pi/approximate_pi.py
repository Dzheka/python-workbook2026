pi = 3.0
print(f"Approximation 1: {pi}")
n = 2
sign = 1
for i in range(2, 16):
    term = 4 / (n * (n + 1) * (n + 2))
    pi = pi + sign * term
    print(f"Approximation {i}: {pi}")
    sign = sign * -1
    n = n + 2