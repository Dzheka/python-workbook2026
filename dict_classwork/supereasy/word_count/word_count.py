def count_words(text):
    a = {}

    for i in text.lower().split():
        a[i] = a.get(i, 0) + 1

    return a


def unique_words(text):
    a = []

    for i, b in count_words(text).items():
        if b == 1:
            a.append(i)

    return sorted(a)

