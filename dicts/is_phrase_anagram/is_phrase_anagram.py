def is_phrase_anagram(phrase1: str, phrase2: str) -> bool:
    clean1 = phrase1.lower().replace(" ", "")
    clean2 = phrase2.lower().replace(" ", "")
    return sorted(clean1) == sorted(clean2)


if __name__ == "__main__":
    print(is_phrase_anagram("listen", "silent"))
    print(is_phrase_anagram("conversation", "voices rant on"))
    print(is_phrase_anagram("The Eyes", "They See"))
    print(is_phrase_anagram("hello world", "world peace"))
    print(is_phrase_anagram("abc", "a b c"))
    print(is_phrase_anagram("", ""))
