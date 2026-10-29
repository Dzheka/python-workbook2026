def two_list_sum(list1: list[int], list2: list[int]):
    a = []

    for i in range(len(list1)):
        a.append(list1[i] + list2[i])

    return a
