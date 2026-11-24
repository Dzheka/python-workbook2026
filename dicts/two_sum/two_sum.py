def two_sum(nums: list[int], target: int) -> list[int] | None:
    seen = {}

    for i, num in enumerate(nums):
        temp = target - num
        if temp in seen:
            return [seen[temp], i]
        seen[num] = i
    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
    print(two_sum([3, 2, 4], 6))            # [1, 2]
    print(two_sum([3, 3], 6))               # [0, 1]
    print(two_sum([2, 3, 5], 10))           # None
    print(two_sum([-1, -2, -3, -4], -5))    # [1, 2]
    print(two_sum([0, 1, 0], 0))            # [0, 2]