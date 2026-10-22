import math
def quadratic_roots(a,b,c):
    d=(b*b)-4*a*c
    if d<0:
        return None
    elif d==0:
        return -b/(2*a)
    return (-b+math.sqrt(d))/(2*a) , (-b-math.sqrt(d))/(2*a)
    
