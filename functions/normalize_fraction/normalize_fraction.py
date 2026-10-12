from math import gcd

def normalize_fraction(numerator, denominator):

    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    return numerator, denominator