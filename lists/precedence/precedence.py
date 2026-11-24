def precedence(operation: str) -> int:
    chars = [' ', '+-', '*/', '^', '~']
    for i in chars:
        for j in i:
            if j == operation:
                return chars.index(i)
    return -1

if __name__ == "__main__":
    # Test your function
    print(precedence('+'))  # 1
    print(precedence('-'))  # 1
    print(precedence('*'))  # 2
    print(precedence('/'))  # 2
    print(precedence('^'))  # 3
    print(precedence('~'))  # 4 (unary minus)