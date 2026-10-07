def number_of_digits(n):
    n = abs(n)
    if n == 0:
        return 1

    count = 0
    while n > 0:
        n //=10
        count+=1
    return(count)
print(number_of_digits(123))
print(number_of_digits(0))
print(number_of_digits(-456))
print(number_of_digits(1000000))
print(number_of_digits(7))