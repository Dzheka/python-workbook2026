def positives(nums):
    return sorted([num for num in nums if num > 0 ])

def has_negative(nums):
    return any(num < 0 for num in nums)