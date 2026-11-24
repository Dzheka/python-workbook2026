def is_anagram(word1, word2):
    a = {}
    b = {}

    for i in word1:
        a[i] = a.get(i, 0) + 1

    for j in word2:
        b[j] = b.get(j, 0) + 1

    return a == b