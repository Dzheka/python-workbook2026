def count_vowels(text):
    text = text.lower()
    vowels = "aeiou"

    count = 0
    for char in text:
        if char in vowels:
            count += 1

    return count


def count_consonants(text):
    text = text.lower()
    vowels = "aeiou"

    count = 0
    for char in text:
        if "a" <= char <= "z":
            if char not in vowels:
                count += 1

    return count


def more_vowels(text):
    vowels_count = count_vowels(text)
    consonants_count = count_consonants(text)

    return vowels_count > consonants_count