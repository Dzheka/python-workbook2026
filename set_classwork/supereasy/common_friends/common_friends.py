def common(a, b):
    return sorted(set(a) & set(b))

def only_first(a, b):
    return sorted(set(a) - set(b))
