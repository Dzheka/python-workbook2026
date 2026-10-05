a = int(input())
if a < 2:
    print('error')
b = 2
while b <= a:
    if a % b == 0:
        print(b)
        a = a // b
    else:
        b+= 1