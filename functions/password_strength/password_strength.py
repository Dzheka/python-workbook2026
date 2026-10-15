def password_strength(pwd):
    lower = 0
    upper = 0
    digit = 0
    special = 0

    for c in pwd:
        if 'a' <= c <= 'z':
            lower = 1
        elif 'A' <= c <= 'Z':
            upper = 1
        elif '0' <= c <= '9':
            digit = 1
        elif c in "!@#$%^&*()_+-=[]{}|;:,.<>?":
            special = 1

    types = lower + upper + digit + special

    if len(pwd) < 8 or types < 2:
        return "weak"
    elif len(pwd) >= 12 and types >= 3:
        return "strong"
    else:
        return "medium"