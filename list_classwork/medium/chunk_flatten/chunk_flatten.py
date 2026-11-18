def chunk(items, size):
    a = []
    for i in range(0, len(items), size):
        a.append(items[i:i + size])
    return a


def flatten(nested):
    a = []
    for i in nested:
        for j in i:
            a.append(j)
    return a


def interleave(a, b):
    x = []

    for i in range(max(len(a), len(b))):
        if i < len(a):
            x.append(a[i])
        if i < len(b):
            x.append(b[i])

    return x