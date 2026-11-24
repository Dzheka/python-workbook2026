def first_repeat(items):
    a = set()

    for i in items:
        if i in a:
            return i
        a.add(i)

    return None


def remove_repeats(items):
    a = set()
    b = []

    for i in items:
        if i not in a:
            a.add(i)
            b.append(i)

    return b