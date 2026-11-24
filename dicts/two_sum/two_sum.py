def two_sum(nums: list[int], target: int):
    s = {}

    for i, n in enumerate(nums):
        k = target - n

        if k in s:
            return [s[k], i]

        s[n] = i

    return None

