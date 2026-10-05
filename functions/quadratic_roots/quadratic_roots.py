from math import sqrt
def quadratic_roots(a, b, c):
    delta  = b*b - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return  -b / (2 * a)
    else:
        return ((-b + sqrt(delta)) / (2 *a), (-b - sqrt(delta)) / (2 *a))