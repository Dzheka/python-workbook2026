def hex_decimal(hex_str: str) -> int:
    hex_str = hex_str.upper()
    digits = "0123456789ABCDEF"
    decimal_value = 0
    
    for char in hex_str:
        if char not in digits:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        value = digits.index(char)
        decimal_value = decimal_value * 16 + value
        
    return decimal_value
