def digit_sum(n):
    n = abs(n)
    total = 0
    while n > 0:
        total+=n % 10
        n //=10
    return(total)

print(digit_sum(123))



    

