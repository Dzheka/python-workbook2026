def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def is_lucky(ticket):
    left = ticket // 1000
    right = ticket % 1000
    return digit_sum(left) == digit_sum(right)


a = int(input())
b = int(input())

count = 0
for ticket in range(a, b + 1):
    if is_lucky(ticket):
        count += 1

print(count)