def filter_list(l: list, condition):
    a = []

    for i in l:
        if condition(i):
            a.append(i)

    return a
