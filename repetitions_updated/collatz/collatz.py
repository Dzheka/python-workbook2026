# Read first number
n = int(input())

# Loop until user enters n <= 0
while n > 0:
    # Display the sequence starting with n
    print(n, end=" ")

    # Generate sequence until reaching 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n, end=" ")

    print()  # New line after sequence

    # Read next number
    n = int(input())
