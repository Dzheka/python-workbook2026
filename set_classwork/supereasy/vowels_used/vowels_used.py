def vowels_in(word):
    vowels = 'aeiou'
    res = []
    for i in word.lower():
        if i in vowels:
           res.append(i)
    return sorted(set(res))

def missing_vowels(word):
    vowels = 'aeiou'
    vowels_in_word = vowels_in(word)
    res = []
    for i in vowels:
        if i not in vowels_in_word:
            res.append(i)
    return sorted(set(res))