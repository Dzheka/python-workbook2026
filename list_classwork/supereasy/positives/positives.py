def positives(nums: list[int]) -> list[int]:
    result = []
    for n in nums:
        if n > 0:
            result.append(n)
    return result


def has_negative(nums: list[int]) -> bool:
    for n in nums:
        if n < 0:
            return True
    return False