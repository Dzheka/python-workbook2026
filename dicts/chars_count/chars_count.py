def chars_count(text: str) -> dict[str, int]:
    r = {}
    for i in text:
        r[i] = r.get(i, 0) + 1
    return r
print(chars_count("hello"))