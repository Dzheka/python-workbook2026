def mark_unary(tokens: list[str]) -> list[str]:
    result = []
    preceding_tokens = {"(", "+", "-", "*", "/", "^", "~"}

    for i, token in enumerate(tokens):
        if token == "-" and (i == 0 or tokens[i - 1] in preceding_tokens):
            result.append("~")
        else:
            result.append(token)

    return result