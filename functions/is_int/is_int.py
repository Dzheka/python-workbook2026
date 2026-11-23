def is_int(s):
    if s == "":
        return False

    if s[0] == "+" or s[0] == "-":
        s = s[1:]

    if s == "":
        return False

    for char in s:
        if char not in "0123456789":
            return False

    return True
print(is_int("123"))