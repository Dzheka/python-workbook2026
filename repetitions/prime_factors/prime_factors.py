n = int(input())

if n < 2:
    print("Error: Number must be 2 or greater")
else:
    print(f"The prime factors of {n} are:")

    factor = 2

    while factor <= n:
        if n % factor == 0:
            # every smaller factor was already divided out, so this one is prime
            print(factor)
            n = n // factor
        else:
            factor += 1
