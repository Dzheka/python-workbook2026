def is_isogram(text: str):
    a = set()

    for i in text.lower():
        if i in " -":
            continue
        if i in a:
            return False
        a.add(i)

    return True

