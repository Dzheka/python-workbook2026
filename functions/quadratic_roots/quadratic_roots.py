import math  
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c 
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1=(-b + math.sqrt(discriminant) )/(2*a) 
        root2=(-b - math.sqrt (discriminant) )/(2*a)
        return(root1,root2)
print(quadratic_roots(1, -3, 2))


