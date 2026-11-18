def greet_all(names):
    a = []

    for i in names:
        a.append(f"Hello, {i}!")

    return a


def count_long_names(names):
    a = 0

    for i in names:
        if len(i) > 4:
            a += 1

    return a