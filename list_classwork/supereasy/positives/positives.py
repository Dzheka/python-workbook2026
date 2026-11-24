def positives(nums):
    a = []

    for i in nums:
        if i > 0:
            a.append(i)

    return a


def has_negative(nums):
    for i in nums:
        if i < 0:
            return True
    return False