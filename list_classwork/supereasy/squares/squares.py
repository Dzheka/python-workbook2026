def squares(n):
    a = []

    for i in range(1, n + 1):
        a.append(i * i)

    return a


def list_sum(nums):
    a = 0

    for i in nums:
        a += i

    return a