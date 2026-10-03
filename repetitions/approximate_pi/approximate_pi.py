pi = 3.0
n = 2
sign = 1
print("Approximation 1:", pi)
for i in range(2, 16):
    pi += sign * 4 / (n * (n + 1) * (n + 2))
    print(f"Approximation {i}: {pi}")
    sign = -sign
    n += 2