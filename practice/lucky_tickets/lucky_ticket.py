def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
        if len(str(n)) == 3:
            break
    if total == sum(int(d) for d in str(n)):
        return True
    return False
