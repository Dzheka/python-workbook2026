def binary_search(items: list, target):
    l = 0
    r = len(items) - 1
    while l <= r:
        m = l + (r - l) // 2

        if items[m] == target:
            return m
        elif items[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1

