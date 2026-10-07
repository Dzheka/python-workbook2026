def password_strength(pwd):
    lower = False
    upper = False
    digit = False
    special = False
    for simbol in pwd:
        if simbol.islower():
            lower = True
        elif simbol.isupper():
            upper = True
        elif simbol.isdigit():
            digit = True
        elif simbol in "!@#$%^&*()_+-=[]{}|;:,.<>?":
            special = True

        types=lower + upper + digit + special
    if len(pwd) >=12 and types>=3:
        return "strong"
    elif len(pwd) >= 8 and types>=2:
        return "medium"
    else:
        return "weak"
print(password_strength("abc"))
     

