from collections import Counter as counter
def first_unique_char(text: str) -> str | None:
    freq = counter(text)
    for i in text:
        if  freq[i] == 1:
            return i
    return None


if __name__ == "__main__":
    print(first_unique_char("leetcode"))  # 'l'
    print(first_unique_char("loveleetcode"))  # 'v'
    print(first_unique_char("aabbcc"))  # None
    print(first_unique_char("abcab"))  # 'c'
    print(first_unique_char("a"))  # 'a'
    print(first_unique_char(""))  # None


if __name__ == "__main__":
    print(first_unique_char("leetcode"))  # 'l'
    print(first_unique_char("loveleetcode"))  # 'v'
    print(first_unique_char("aabbcc"))  # None
    print(first_unique_char("abcab"))  # 'c'
    print(first_unique_char("a"))  # 'a'
    print(first_unique_char(""))  # None