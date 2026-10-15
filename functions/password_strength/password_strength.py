def password_strength(p):
    if len(p) <8 or p.isdigit() or p.isalpha():
        return "weak"
    elif len(p) >= 8 and len(p) <12:
        return "medium"
    else:
        return "strong"   
print(password_strength("Hello123"))
