def find_missing(numbers: list, n: int) -> list:
    a = set()
    for i in numbers:
        a.add(i)

    b = []
    for i in range(1, n + 1):
        if i not in a:
            b.append(i)

    return b
