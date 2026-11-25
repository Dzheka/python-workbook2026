def first_unique_char(text: str) -> str | None:
    c = {}
    for i in text:
        c[i] = c.get(i, 0) + 1
    for i in text:
        if c[i] == 1:
            return i
    return None
print(first_unique_char("leetcode"))