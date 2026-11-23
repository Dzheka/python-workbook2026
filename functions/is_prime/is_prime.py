import math
def is_prime(n):
    if n==2 :
        return True
    elif n==1 or n==0 or n==-5:
        return False
    n=abs(n)
    for i in range(2,n):
        if n%i==0:
            return False
    return True
