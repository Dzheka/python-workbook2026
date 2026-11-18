def sort_numbers(numbers: list[int]) -> list[int]:
    result = []
    copy = numbers.copy()
    for i in range(len(copy)):
        m = min(copy)
        copy.remove(m)
        result.append(m)
    return  result



if __name__ == "__main__":
    # Test your function
    print(sort_numbers([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
    print(sort_numbers([5, 2, 3]))        # [2, 3, 5]