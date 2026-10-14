def to_base(n: int, base: int) -> str:
    if not 2 <= base <= 36:
        raise ValueError("Base must be between 2 and 36 inclusive.")
        
    if n == 0:
        return "0"
        
    is_negative = n < 0
    n = abs(n)
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    while n > 0:
        n, remainder = divmod(n, base)
        result.append(digits[remainder])
        
    if is_negative:
        result.append("-")
        
    return "".join(reversed(result))
