def precedence(op: str) -> int:
    if op in ("+", "-"):
        return 1
    if op in ("*", "/", "//", "%"):
        return 2
    if op in ("^", "**"):
        return 3
    return 0


def infix_to_postfix(tokens: list[str]) -> list[str]:
    output = []
    stack = []
    operators = {"+", "-", "*", "/", "//", "%", "^", "**"}

    for token in tokens:
        if token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack:
                stack.pop()
        elif token in operators:
            while (
                stack
                and stack[-1] != "("
                and precedence(stack[-1]) >= precedence(token)
            ):
                output.append(stack.pop())
            stack.append(token)
        else:
            output.append(token)

    while stack:
        output.append(stack.pop())

    return output
