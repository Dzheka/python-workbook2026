def sublists(l: list) -> list[list]:
    result = [[]]
    for length in range(1, len(l) + 1):
        for start in range(len(l) - length + 1):
            result.append(l[start:start + length])
    return result