def letters_in(word):
    return {i for i in word.lower() if i.isalpha()}


def common_letters(words):
    if not words:
        return []

    a = letters_in(words[0])
    for i in words[1:]:
        a &= letters_in(i)

    return sorted(a)


def any_letters(words):
    a = set()
    for i in words:
        a |= letters_in(i)

    return sorted(a)