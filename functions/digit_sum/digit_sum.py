def digit_sum(n):
    c=0
    while abs(n) >= 1:
        c=c+n%10
        c=c//10
    return c
print(digit_sum(123))
    
        

