def tokenize_expression(expr: str) -> list[str]:
    a = []
    b = ""

    for i in expr:
        if i.isdigit():
            b += i
        else:
            if b:
                a.append(b)
                b = ""

            if i.isspace():
                continue

            if i in "+-*/^()":
                a.append(i)
            else:
                raise ValueError(f"Unknown character: {i}")

    if b:
        a.append(b)

    return a