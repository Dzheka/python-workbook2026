from collections import Counter
def chars_count(text: str) -> dict[str, int]:
    obj = {}
    for i in text:
        if i not in obj:
            obj[i] = 1
        else:
            obj[i] += 1
    return obj


if __name__ == "__main__":
    print(chars_count("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(chars_count(""))  # {}
    print(chars_count("aaa"))  # {'a': 3}
    print(chars_count("hello world"))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    print(chars_count("AaBbCc"))  # {'A': 1, 'a': 1, 'B': 1, 'b': 1, 'C': 1, 'c': 1}
    print(chars_count("12321"))  # {'1': 2, '2': 2, '3': 1}