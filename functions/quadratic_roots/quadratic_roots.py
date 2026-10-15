def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  
    elif discriminant == 0:
        root = -b / (2*a)
        return (root)  
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)  