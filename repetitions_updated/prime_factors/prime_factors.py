# Read integer from user
n = int(input())

# Check if less than 2
if n < 2:
    print("Error: Number must be 2 or greater")
else:
    print(f"The prime factors of {n} are:")

    # Initialize factor to 2
    factor = 2

    # Loop while factor <= n
    while factor <= n:
        if n % factor == 0:
            # factor is a prime factor
            print(factor)
            n = n // factor
        else:
            # Increase factor
            factor += 1
