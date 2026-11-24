def normalize_fraction(numerator, denominator):
    if numerator == 0:
        return (0, 1)
    a = abs(numerator)
    b = abs(denominator)

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    gcd = a
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd

    return (simplified_numerator, simplified_denominator)