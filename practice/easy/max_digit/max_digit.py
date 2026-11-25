def max_digit(n):
    c=0
    while abs(n)>0:
        if abs(n)%10>c:
            c=abs(n)%10
        n=abs(n)//10
    return c
def min_digit(n):
    if n==0:
        return 0
    d=9
    while abs(n)>0:
        if abs(n)%10<d:
            d=abs(n)%10
        n=abs(n)//10
    return d
def digit_range(n):
    return max_digit(n) - min_digit(n)
