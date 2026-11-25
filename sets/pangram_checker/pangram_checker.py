def is_pangram(text: str):
    a = set()

    for i in text.lower():
        if i in "abcdefghijklmnopqrstuvwxyz":
            a.add(i)

    return len(a) == 26