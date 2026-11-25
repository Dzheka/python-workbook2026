def is_anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)