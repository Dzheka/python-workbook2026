def list_total(numbers: list[int]) -> int:
    total = 0
    for i in numbers:
        total += i
    return total



if __name__ == "__main__":
    # Test your function
    print(list_total([2, 3, 5, 7, 11]))  # 28
    print(list_total([10, -5, 3]))       # 8
    print(list_total([]))                # 0
