def is_phrase_anagram(phrase1: str, phrase2: str) -> bool:
    def clean(s):
        return sorted(c.lower() for c in s if c != ' ')
    return clean(phrase1) == clean(phrase2)
print(is_phrase_anagram("listen", "silent"))