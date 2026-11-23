def number_of_digits(n):
    count = 0
    n = str(n)
    for i in n:
        if i.isdigit():
            count += 1
        else:
            continue
    return count
print(number_of_digits(-123))
