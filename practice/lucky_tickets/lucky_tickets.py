def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def is_lucky(ticket):
    return digit_sum(ticket // 1000) == digit_sum(ticket % 1000)

a = int(input())
b = int(input())

count = 0
for ticket in range(a, b + 1):
    if is_lucky(ticket):
        count += 1

print(count)



