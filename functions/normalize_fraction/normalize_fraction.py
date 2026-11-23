def normalize_fraction(numerator, denominator):
     for i in range(2, numerator + 1):
         while numerator % i == 0 and denominator % i == 0:
             return normalize_fraction(numerator // i, denominator // i)
     for i in range(2, denominator + 1):
         while numerator % i == 0 and denominator % i == 0:
             return normalize_fraction(numerator // i, denominator // i)
     return numerator, denominator