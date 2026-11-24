def is_isogram(text: str) -> bool:
    seen = set()

    for i in text.lower():
        if not i.isalpha():
            continue
        if i in seen:
            return False
        else:
            seen.add(i)
    return True


if __name__ == "__main__":
    print(is_isogram("lumberjacks"))  # True
    print(is_isogram("isograms"))  # False
    print(is_isogram("Alphabet"))  # False
    print(is_isogram("thumbscrew-japingly"))  # True
    print(is_isogram("Emily Jung Schwartzkopf"))  # True
    print(is_isogram(""))  # True