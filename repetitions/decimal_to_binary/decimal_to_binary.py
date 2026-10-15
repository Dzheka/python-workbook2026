n = int(input())

if n == 0:
    result = "0"
else:
    result = ""

    # Each remainder is the next binary digit from the right, hence the prepend
    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n = n // 2

print(result)
