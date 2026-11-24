def chars_count(text):
    a = {}

    for i in text:
        a[i] = a.get(i, 0) + 1

    return a