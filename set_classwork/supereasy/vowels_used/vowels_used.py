VOWELS = set("aeiou")


def vowels_in(word):
    letters = set(word.lower())
    return sorted(VOWELS & letters)


def missing_vowels(word):
    letters = set(word.lower())
    return sorted(VOWELS - letters)