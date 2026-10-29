def evaluate_postfix(tokens: list[str]) -> float:
    a = []

    for token in tokens:
        if token in ('+', '-', '*', '/', '^'):
            b = a.pop()
            c = a.pop()

            if token == '+':
                a.append(c + b)
            elif token == '-':
                a.append(c - b)
            elif token == '*':
                a.append(c * b)
            elif token == '/':
                a.append(c / b)
            else:
                a.append(c ** b)
        else:
            a.append(float(token))

    return a.pop()