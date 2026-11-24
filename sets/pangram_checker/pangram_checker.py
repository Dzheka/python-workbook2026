def is_pangram(text: str) -> bool:
    seen = set()

    for i in text.lower():
        if not i.isalpha():
            continue
        if i not in seen:
            seen.add(i)
    return True if len(seen) == 26 else False



if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
    print(is_pangram("Pack my box with five dozen liquor jugs"))  # True
    print(is_pangram("Hello World"))  # False
    print(is_pangram("abcdefghijklmnopqrstuvwxyz"))  # True
    print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # True