def positives(nums):
    result = []
    for n in nums:
        if n > 0:
            result.append(n)
    return result


def has_negative(nums):
    for n in nums:
        if n < 0:
            return True
    return False