def digit_sum(n):
    c=0
    while abs(n)>0:
        c=c+abs(n)%10
        n=abs(n)//10
    return c
print (digit_sum(1233))