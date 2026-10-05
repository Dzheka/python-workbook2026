# Read decimal number
q = int(input())

# Handle special case of 0
if q == 0:
    result = "0"
else:
    # Initialize result as empty string
    result = ""

    # Convert to binary using division algorithm
    while q > 0:
        r = q % 2
        result = str(r) + result
        q = q // 2

# Display result
print(f"The binary equivalent is {result}")
