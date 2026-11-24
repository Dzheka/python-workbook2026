def precedence(operation: str):
    a = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '~': 4,
    }
    return a[operation]