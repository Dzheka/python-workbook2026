def max_digit(n):
    n = abs(n)
    s = str(n)
    biggest = int(s[0])
    for i in str(n):
        ns = int(i)
        if biggest < ns:
            biggest = ns
    return biggest

def min_digit(n):
    n = abs(n)
    s = str(n)
    minimum = int(s[0])
    for i in str(n):
        ns = int(i)
        if minimum > ns:
            minimum = ns
    return minimum

def digit_range(n):
    return max_digit(n) - min_digit(n)
