def sublists(l: list) -> list[list]:
    result = [[]]

    for size in range(1, len(l) + 1):
        for start in range(len(l) - size + 1):
            result.append(l[start:start + size])

    return result

if __name__ == "__main__":
    # Test your function
    print(sublists([2, 3, 5]))
    # [[], [2], [3], [5], [2, 3], [3, 5], [2, 3, 5]]