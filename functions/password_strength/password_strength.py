def password_strength(pwd: str) -> str:
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for c in pwd:
        if c.islower():
            has_lower = True
        elif c.isupper():
            has_upper = True
        elif c.isdigit():
            has_digit = True
        elif c in special_chars:
            has_special = True

    types_count = sum([has_lower, has_upper, has_digit, has_special])

    if len(pwd) >= 12 and types_count >= 3:
        return "strong"
    elif len(pwd) >= 8 and types_count >= 2:
        return "medium"
    else:
        return "weak"