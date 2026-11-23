from collections import Counter
def most_frequent_char(text: str) -> str:
    obj = Counter(text)
    maximum = max(obj.values())

    for k, v in obj.items():
        if v == maximum:
            return k
    return None




if __name__ == "__main__":
    print(most_frequent_char("hello"))  # 'l'
    print(most_frequent_char("aabbcc"))  # 'a' (or 'b' or 'c' - all tied)
    print(most_frequent_char("a"))  # 'a'
    print(most_frequent_char("AaA"))  # 'A'
    print(most_frequent_char("hello world"))  # 'l'