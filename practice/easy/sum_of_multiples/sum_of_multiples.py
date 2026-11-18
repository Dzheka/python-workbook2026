def count_multiples(limit, a, b):
    c = 0
    for n in range(1, limit):
        if n % a == 0 or n % b == 0:
            c += 1
    return c


def sum_multiples(limit, a, b):
    d = 0
    for n in range(1, limit):
        if n % a == 0 or n % b == 0:
            d += n
    return d