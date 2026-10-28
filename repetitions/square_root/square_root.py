n = int(input())
g = n /2
while abs(g ** 2 - n) > 1e-12:
    g = (g + n / g) / 2
print(round(g, 10))