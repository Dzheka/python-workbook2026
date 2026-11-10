def squares(n):
    return [num ** 2 for num in range(1, n + 1)]

def list_sum(nums):
    total = 0
    for i in nums:
        total += i
    return total