def sublists(l: list) -> list[list]:
    a = [[]]

    for j in range(1, len(l) + 1):
        for i in range(len(l) - j + 1):
            a.append(l[i:i + j])

    return a