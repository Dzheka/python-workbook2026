n = int(input())
if n < 2:
    print('Error: Number must be 2 or greater')
    exit()

print(f"The prime factors of {int(n)} are:")
while n != 1:
    n = int(n)
    if n % 2 == 0:
        n = n // 2
        print(2)
    elif n % 3 == 0:
        n = n // 3
        print(3)
    else:
        print(n)
        break
