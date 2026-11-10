def is_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    return False
