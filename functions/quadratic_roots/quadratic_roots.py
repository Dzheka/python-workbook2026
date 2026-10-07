import math
def quadratic_roots(a,b,c):
    if b*b-4*a*c < 0:
        return None
    elif b**2 - 4*a*c >0:
        r1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        r2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return (r1,r2)
    else:
        return -b/(2*a)
print(quadratic_roots(1,2,1))

