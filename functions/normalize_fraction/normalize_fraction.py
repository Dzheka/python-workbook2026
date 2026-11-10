def normalize_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
        
    if numerator == 0:
        return (0, 1)
        
    a, b = abs(numerator), abs(denominator)
    while b:
        a, b = b, a % b
    gcd = a
    
    simplified_num = numerator // gcd
    simplified_den = denominator // gcd
    
    if simplified_den < 0:
        simplified_num = -simplified_num
        simplified_den = -simplified_den
        
    return (simplified_num, simplified_den)
