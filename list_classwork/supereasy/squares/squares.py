def squares(n):
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result


def list_sum(nums):
    result = 0
    for num in nums:
        result += num
    return result