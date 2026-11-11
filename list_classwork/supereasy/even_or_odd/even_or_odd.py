def even_or_odd(nums):
    copy = nums.copy()
    for i in range(0, len(nums)):
        if copy[i] % 2 == 0:
            copy[i] = 'even'
        else:
            copy[i] = 'odd'
    return copy

def count_even(nums):
    even_n = 0
    nums = even_or_odd(nums)
    for i in nums:
        if i == 'even':
            even_n += 1
    return even_n
