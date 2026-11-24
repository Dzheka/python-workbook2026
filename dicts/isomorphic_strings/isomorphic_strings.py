from collections import Counter
def isomorphic_strings(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for ch_s, ch_t in zip(s, t):
        if ch_s in s_to_t and s_to_t[ch_s] != ch_t:
            return False
        if ch_t in t_to_s and t_to_s[ch_t] != ch_s:
            return False

        s_to_t[ch_s] = ch_t
        t_to_s[ch_t] = ch_s

    return True


if __name__ == "__main__":
    print(isomorphic_strings("egg", "add"))  # True
    print(isomorphic_strings("foo", "bar"))  # False
    print(isomorphic_strings("paper", "title"))  # True
    print(isomorphic_strings("ab", "abc"))  # False
    print(isomorphic_strings("abc", "abc"))  # True
    print(isomorphic_strings("", ""))  # True