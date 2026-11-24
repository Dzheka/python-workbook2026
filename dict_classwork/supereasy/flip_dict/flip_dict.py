def invert(d):
    a = {}

    for i, b in d.items():
        a[b] = i

    return a

def keys_for(d, value):
    a = []
    for i, b in d.items():
        if b == value:
            a.append(i)
    return sorted(a)