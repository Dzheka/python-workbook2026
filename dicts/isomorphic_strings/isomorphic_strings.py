def isomorphic_strings(s: str, t: str):
    if len(s) != len(t):
        return False

    m = {}
    u = set()

    for a, b in zip(s, t):
        if a in m:
            if m[a] != b:
                return False
        else:
            if b in u:
                return False

            m[a] = b
            u.add(b)

    return True

