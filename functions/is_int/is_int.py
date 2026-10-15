def is_int(s):
    if not s:
        return False

    if s[0] in ('+', '-'):
        s = s[1:]

    return s.isdigit()