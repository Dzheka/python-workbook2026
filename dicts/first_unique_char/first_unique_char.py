def first_unique_char(text: str) -> str | None:
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for char, count in freq.items():
        if count == 1:
            return char
    return None



if __name__ == "__main__":
    print(first_unique_char("leetcode"))  # 'l'
    print(first_unique_char("loveleetcode"))  # 'v'
    print(first_unique_char("aabbcc"))  # None
    print(first_unique_char("abcab"))  # 'c'
    print(first_unique_char("a"))  # 'a'
    print(first_unique_char(""))  # None
