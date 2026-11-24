def first_unique_char(text):
    a = {}

    for i in text:
        a[i] = a.get(i, 0) + 1

    for j in text:
        if a[j] == 1:
            return j

    return None