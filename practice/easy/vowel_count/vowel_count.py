def count_vowels(text):
    count = 0
    for i in text.lower():
        if i in "aeiou":
            count += 1
    return count


def count_consonants(text):
    count = 0
    for i in text.lower():
        if "a" <= i <= "z" and i not in "aeiou":
            count += 1
    return count


def more_vowels(text):
    return count_vowels(text) > count_consonants(text)