integer = int(input())
if integer < 2:
    print('error')
factor = 2
while factor <= integer:
    if integer % factor == 0:
        print(factor)
        integer = integer // factor
    else:
        factor+= 1