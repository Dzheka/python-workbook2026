def isomorphic_strings(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_s = {}
    map_t = {}
    for a, b in zip(s, t):
        if a in map_s:
            if map_s[a] != b:
                return False
        else:
            map_s[a] = b
        if b in map_t:
            if map_t[b] != a:
                return False
        else:
            map_t[b] = a
    return True
print(isomorphic_strings("egg", "add"))