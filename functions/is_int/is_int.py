def is_int(s: str) -> bool:
    if not s:
        return False
        
    if s[0] in ('+', '-'):
        s = s[1:]
        
    return len(s) > 0 and s.isdigit()
