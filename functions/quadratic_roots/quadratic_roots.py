import math

def quadratic_roots(a, b, c) -> tuple:
    dscr = b** 2 - 4 * a * c
    if dscr < 0:
        return None
    elif dscr == 0:
        root1 = -b / (2 * a)
        return root1
    elif dscr > 0:
        root1 = (-b + math.sqrt(dscr)) / (2 * a)
        root2 = (-b - math.sqrt(dscr)) / (2 * a)
        return root1, root2

print(quadratic_roots(1, 0, -4))
