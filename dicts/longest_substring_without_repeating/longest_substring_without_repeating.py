def longest_substring_without_repeating(s: str):
    k = {}
    l = 0
    b = 0

    for r, c in enumerate(s):
        if c in k and k[c] >= l:
            l = k[c] + 1

        k[c] = r
        b = max(b, r - l + 1)

    return b


