def most_frequent_char(text: str) -> str:
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return max(freq, key=lambda k: freq[k])


if __name__ == "__main__":
    print(most_frequent_char("hello"))  # 'l'
    print(most_frequent_char("aabbcc"))  # 'a'
    print(most_frequent_char("a"))  # 'a'
    print(most_frequent_char("AaA"))  # 'A'
    print(most_frequent_char("hello world"))  # 'l'
