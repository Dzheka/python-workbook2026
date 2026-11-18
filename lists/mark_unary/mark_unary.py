def mark_unary(tokens: list[str]) -> list[str]:
    a: list[str] = []
    b = {'+', '-', '*', '/', '^', '~'}

    for i, token in enumerate(tokens):
        if token == '-' and (
            i == 0
            or tokens[i - 1] == '('
            or tokens[i - 1] in b
        ):
            a.append('~')
        else:
            a.append(token)

    return a