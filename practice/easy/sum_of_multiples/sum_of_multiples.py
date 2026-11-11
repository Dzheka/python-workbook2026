def count_multiples(limit, a, b):
    count = 0
    for i in range(1, limit):
        if i % a == 0 or i % b == 0:
            count += 1
    return count

def sum_multiples(limit, a, b):
    total_sum = 0
    for i in range(1, limit):
        if i % a == 0 or i % b == 0:
            total_sum += i
    return total_sum