def gcd(n,m):
    i=max(n,m)
    while(i>1):
        if n%i==0 and m%i==0:
            return i
        i-=1
    return 1

def normalize_fraction(num , denom):
    g=gcd(num,denom)
    num//=g
    denom//=g
    return (num,denom)
    
