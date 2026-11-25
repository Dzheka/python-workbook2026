def two_sum(nums: list[int], target: int) -> list[int] | None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    print(two_sum([2, 3, 5], 10))
    print(two_sum([-1, -2, -3, -4], -5))
    print(two_sum([0, 1, 0], 0))
