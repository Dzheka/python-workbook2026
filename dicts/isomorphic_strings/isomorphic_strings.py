def isomorphic_strings(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False

        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True


if __name__ == "__main__":
    print(isomorphic_strings("egg", "add"))  # True
    print(isomorphic_strings("foo", "bar"))  # False
    print(isomorphic_strings("paper", "title"))  # True
    print(isomorphic_strings("ab", "abc"))  # False
    print(isomorphic_strings("abc", "abc"))  # True
    print(isomorphic_strings("", ""))  # True
