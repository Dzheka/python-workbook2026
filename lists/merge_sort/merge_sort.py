def merge_sort(list1: list[int], list2: list[int]):
    a: list[int] = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            a.append(list1[i])
            i += 1
        else:
            a.append(list2[j])
            j += 1

    a.extend(list1[i:])
    a.extend(list2[j:])

    return a