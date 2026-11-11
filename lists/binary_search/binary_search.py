def binary_search(items: list, target) -> int:
    low = 0
    high = len(items) - 1
    mid = low + (high - low) // 2

    while low <= high:
        if items[mid] == target:
            return mid
        elif items[mid] > target:
            high = mid - 1
        elif items[mid] < target:
            low = mid + 1
        mid = low + (high - low) // 2
    return -1


if __name__ == "__main__":
    # Test your function
    items = [2, 3, 5, 7, 11]
    print(binary_search(items, 5))  # 2
    print(binary_search(items, 4))  # -1