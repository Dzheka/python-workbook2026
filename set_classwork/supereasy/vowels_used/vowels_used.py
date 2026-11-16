def vowels_in(word: str):
    words = []
    for i in word.lower():
        if i in "aeiou" and i not in words:
            words.append(i)
    return sorted(words)
print(vowels_in("education"))

def missing_vowels(word: str):
    ans = set(word.lower())
    return sorted(set("aeiou") - ans)
print(missing_vowels("rhythm"))