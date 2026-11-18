def even_or_odd(nums):
    a = []

    for i in nums:
        if i % 2 == 0:
            a.append("even")
        else:
            a.append("odd")

    return a


def count_even(nums):
    a = 0

    for i in nums:
        if i % 2 == 0:
            a += 1

    return a