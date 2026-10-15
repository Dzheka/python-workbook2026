# Nilakantha series: pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
approximation = 3.0

print(f"Approximation 1: {approximation}")

for i in range(2, 16):
    n = (i - 1) * 2
    denominator = n * (n + 1) * (n + 2)

    if i % 2 == 0:
        approximation += 4 / denominator
    else:
        approximation -= 4 / denominator

    print(f"Approximation {i}: {approximation}")
