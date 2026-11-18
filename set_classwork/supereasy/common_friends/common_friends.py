def common(a, b):
    ans = set(a) & set(b)
    return sorted(ans)

def only_first(a, b):
    a, b = set(a), set(b)
    return sorted(a - b)