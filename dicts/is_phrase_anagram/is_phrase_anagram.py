def is_phrase_anagram(phrase1, phrase2):
    phrase1 = phrase1.lower().replace(" ", "")
    phrase2 = phrase2.lower().replace(" ", "")

    a = {}
    b = {}

    for i in phrase1:
        a[i] = a.get(i, 0) + 1

    for j in phrase2:
        b[j] = b.get(j, 0) + 1

    return a == b