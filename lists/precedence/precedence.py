def precedence(operation: str) -> int:
    levels = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
        "~": 4,
    }
    return levels.get(operation, 0)