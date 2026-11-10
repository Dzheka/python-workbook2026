def is_pangram(text: str) -> bool:
    ans = set()
    ans = set(text)
    if len(ans) >= 26:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
    print(is_pangram("Pack my box with five dozen liquor jugs"))  # True
    print(is_pangram("Hello World"))  # False
    print(is_pangram("abcdefghijklmnopqrstuvwxyz"))  # True
    print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # True
