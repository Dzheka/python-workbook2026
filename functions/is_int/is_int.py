def is_int(s):
    if s == "":
        return False

    if s[0] == "+" or s[0] == "-":
        s = s[1:]

    if s == "":
        return False

    for i in range(len(s)):
        if s[i] < "0" or s[i] > "9":
            return False

    return True