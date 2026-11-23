from collections import Counter


def is_anagram(word1: str, word2: str) -> bool:
    a = Counter(word1)
    b = Counter(word2)

    for k, v in a.items():
        if k in b:
            if v >= b[k]:
                continue
            else:
                return False
        else:
            return False
    for k, v in b.items():
        if k in a:
            if v >= a[k]:
                continue
            else:
                return False
        else:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))  # False
    print(is_anagram("abc", "abcd"))  # False
    print(is_anagram("test", "test"))  # True
    print(is_anagram("", ""))  # True
    print(is_anagram("a", "a"))  # True