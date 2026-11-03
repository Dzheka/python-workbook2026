def square_digit_sum(n):
    total = 0
    while True:
        total += (n % 10)** 2
        n = n // 10
        return total
print(square_digit_sum(19)) 