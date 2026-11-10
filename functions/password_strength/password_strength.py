def password_strength(pwd: str) -> str:
    if not pwd:
        return "weak"
        
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in special_chars for c in pwd)
    
    types_count = sum([has_lower, has_upper, has_digit, has_special])
    length = len(pwd)
    
    if length >= 12 and types_count >= 3:
        return "strong"
    elif length >= 8 and types_count >= 2:
        return "medium"
        
    return "weak"
