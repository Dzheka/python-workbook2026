import math

def normalize_fraction(numerator, denominator):
    if denominator == 0:
        return None

    divisor = math.gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    return (numerator, denominator)
print(normalize_fraction(4, 8))