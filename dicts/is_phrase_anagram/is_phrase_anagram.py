from collections import Counter


def is_phrase_anagram(phrase1: str, phrase2: str) -> bool:
    a = Counter(phrase1.lower())
    b = Counter(phrase2.lower())

    for k, v in a.items():
        if k == ' ':
            continue
        if k in b:
            if v >= b[k]:
                continue
            else:
                return False
        else:
            return False
    for k, v in b.items():
        if k == ' ':
            continue
        if k in a:
            if v >= a[k]:
                continue
            else:
                return False
        else:
            return False
    return True


if __name__ == "__main__":
    print(is_phrase_anagram("listen", "silent"))  # True
    print(is_phrase_anagram("conversation", "voices rant on"))  # True
    print(is_phrase_anagram("The Eyes", "They See"))  # True
    print(is_phrase_anagram("hello world", "world peace"))  # False
    print(is_phrase_anagram("abc", "a b c"))  # True
    print(is_phrase_anagram("", ""))  # True