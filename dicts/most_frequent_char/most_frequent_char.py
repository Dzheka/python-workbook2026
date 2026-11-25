def most_frequent_char(text):
    a = {}

    for i in text:
        a[i] = a.get(i, 0) + 1

    b = max(a.values())

    for j in a:
        if a[j] == b:
            return j
        