def even_or_odd(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append("even")
        else:
            result.append("odd")
    return result


def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count