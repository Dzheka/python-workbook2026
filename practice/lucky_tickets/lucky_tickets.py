def digit_sum(n):
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)
def is_lucky(ticket):
    if digit_sum(int(str(ticket)[:3])) == digit_sum(int(str(ticket)[-3:])):
        return True
    return False

a = int(input())
b = int(input())
counter = 0
if (100000 <= a <= b <= 999999):
    for i in range(a, b + 1):
        if is_lucky(i):
            counter += 1
print(counter)