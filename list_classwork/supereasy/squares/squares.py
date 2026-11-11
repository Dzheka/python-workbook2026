def squares(n: int) -> list[int]:
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result


def list_sum(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result += num
    return result