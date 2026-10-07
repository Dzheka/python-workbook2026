import math
def number_of_digits(n):
    m = 0
    if n !=0:
        while abs(n)>=1:
            n = n/10
            m+=1
        return m
    else:
        return 1
print(number_of_digits(0))