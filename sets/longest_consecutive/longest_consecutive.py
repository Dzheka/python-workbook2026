def longest_consecutive(numbers: list) -> int:
    num_set = set(numbers)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1


            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)

    return max_length


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 (sequence: 1,2,3,4)
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 (sequence: 0-8)
    print(longest_consecutive([1, 2, 0, 1]))  # 3 (sequence: 0,1,2)
    print(longest_consecutive([]))  # 0
    print(longest_consecutive([5]))  # 1
    print(longest_consecutive([1, 3, 5, 7]))  # 1 (no consecutive numbers)
