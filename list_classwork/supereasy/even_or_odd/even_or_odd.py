def even_or_odd(nums):
    return ["even" if num % 2 == 0 else "odd" for num in nums]

def count_even(nums: list):
    return len([num for num in nums if num % 2 == 0])

