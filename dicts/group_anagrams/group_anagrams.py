def group_anagrams(words):
    a = {}

    for i in words:
        b = "".join(sorted(i))

        if b not in a:
            a[b] = []

        a[b].append(i)

    return list(a.values())