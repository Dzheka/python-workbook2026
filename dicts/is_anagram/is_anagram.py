def is_anagram(word1: str, word2: str) -> bool:
    dict1 = {} 
    dict2 = {}
    for i in word1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in word2:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1
    return dict1 == dict2

if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))  # False
    print(is_anagram("abc", "abcd"))  # False
    print(is_anagram("test", "test"))  # True
    print(is_anagram("", ""))  # True
    print(is_anagram("a", "a"))  # True
